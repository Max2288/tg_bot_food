from django.apps import AppConfig


class FoodFreeAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "food_free_app"

    def ready(self):
        import food_free_app.signals