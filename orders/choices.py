from django.db.models import TextChoices


class StatusChoices(TextChoices):
    Waiting = "Waiting"
    Completed = "Completed"
