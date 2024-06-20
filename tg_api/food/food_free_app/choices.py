from django.db import models


class RoleChoices(models.TextChoices):
    USER = "USER", "USER"
    OPERATOR = "OPERATOR", "OPERATOR"
    ADMIN = "ADMIN", "ADMIN"

    def __str__(self):
        return self.label


class StatusChoices(models.TextChoices):
    CREATED = "CREATED", "CREATED"
    IN_PROGRESS = "IN_PROGRESS", "IN_PROGRESS"
    DONE = "DONE", "DONE"
    CANCELLED = "CANCELLED", "CANCELLED"

    def __str__(self):
        return self.label
