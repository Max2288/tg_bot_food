from django.db import models
from django.contrib.gis.db.models import PointField

from food_free_app.choices import RoleChoices, StatusChoices
from django.utils.translation import gettext_lazy as _

class IDMixin(models.Model):
    """Миксин для добавления поля ID к моделям."""

    id = models.AutoField(primary_key=True, editable=True)

    class Meta:
        abstract = True


class Address(IDMixin):
    country = models.TextField(max_length=100)
    city = models.TextField()
    street = models.TextField()
    building_num = models.IntegerField()
    entrance = models.IntegerField()
    floor = models.IntegerField()
    apartment_number = models.IntegerField()
    coordinates = PointField()

    class Meta:
        db_table = '"food"."address"'
        verbose_name = _('address')


class User(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=True)
    username = models.TextField()

    class Meta:
        db_table = '"food"."user"'
        verbose_name = _('user')


class Shop(IDMixin):
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, db_column='address')

    class Meta:
        db_table = '"food"."shop"'
        verbose_name = _('shop')

    def __str__(self):
        return self.name


class Product(IDMixin):
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    image = models.TextField()
    is_hot = models.BooleanField()
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, db_column='shop')

    class Meta:
        db_table = '"food"."product"'
        verbose_name = _('product')

    def __str__(self):
        return f'Продукт: {self.name} из магазина {self.shop.name}'


class FeedBack(IDMixin):
    score = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, db_column='shop')

    class Meta:
        db_table = '"food"."feedback"'
        verbose_name = _('feedback')


class Subscription(IDMixin):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, db_column='shop')

    class Meta:
        db_table = '"food"."subscription"'
        verbose_name = _('subscription')


class MailingList(IDMixin):
    message = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, db_column='shop')
    date = models.DateTimeField()

    class Meta:
        db_table = '"food"."mailinglist"'
        verbose_name = _('mailinglist')

class MailingMessage(IDMixin):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user')
    shop = models.ForeignKey(Shop, on_delete=models.DO_NOTHING, db_column='shop')
    date = models.DateTimeField()
    status = models.TextField(
        choices=StatusChoices.choices, default=StatusChoices.CREATED
    )

    class Meta:
        db_table = '"food"."mailingmessage"'
        verbose_name = _('mailingmessage')