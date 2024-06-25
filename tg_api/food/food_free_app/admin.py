from django.contrib import admin
from food_free_app.models import *

models_to_register = [
    Address,
    User,
    Shop,
    Product,
    FeedBack,
    Subscription,
    MailingList,
    MailingMessage,
]


for model in models_to_register:
    admin.site.register(model)
