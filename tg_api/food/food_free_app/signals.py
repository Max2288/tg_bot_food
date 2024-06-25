from itertools import islice

from django.db.models.signals import post_migrate
from django.db.utils import IntegrityError
from django.dispatch import receiver
from food_free_app import models
from food_free_app.constants import ADRESES, PRODUCTS, SHOPS


def create_objects(model: models.models, bulk_items: list[dict] = None):
    batch_size = 100
    objs = [model(**item) for item in bulk_items]
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        model.objects.bulk_create(batch, batch_size)


def create_objects_with_skip(model: models.models, bulk_items: list[dict] = None):
    retry_count = 3
    for _ in range(retry_count):
        try:
            create_objects(model, bulk_items)
            break
        except IntegrityError:
            continue


@receiver(post_migrate)
def create_initial_models(sender, **kwargs):
    print("Creating initial models")
    if sender.name == "food_free_app":
        if not models.Address.objects.exists():
            create_objects_with_skip(models.Address, ADRESES)
        if not models.Shop.objects.exists():
            for shop_data in SHOPS:
                shop_data["address"] = models.Address.objects.get(
                    id=shop_data["address"]
                )
            create_objects_with_skip(models.Shop, SHOPS)
        if not models.Product.objects.exists():
            create_objects_with_skip(models.Product, PRODUCTS)
