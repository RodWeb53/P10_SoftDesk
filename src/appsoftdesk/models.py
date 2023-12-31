from django.db import models
from django.conf import settings


class Projects(models.Model):
    class TYPE_CHOICES(models.TextChoices):
        BE = 'back-end'
        FE = 'Front-end'
        IOS = 'IOS'
        AN = 'Android'

    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=70, choices=TYPE_CHOICES.choices)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Contributors(models.Model):
    class PERMISSION_CHOICES(models.TextChoices):
        CREATOR = "Creator"
        CONTRIB = "Contributor"

    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="contributors")
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name="contributors")
    permission = models.CharField(max_length=70, choices=PERMISSION_CHOICES.choices)
    role = models.CharField(max_length=255)

    class Meta:
        unique_together = ['author_user', 'project', ]

    def __str__(self):
        return self.author_user.email


class Issues(models.Model):
    class PRIORITY_CHOICES(models.TextChoices):
        L = "Low"
        M = "Medium"
        H = "High"

    class TAG_CHOICES(models.TextChoices):
        BU = "Bug"
        IM = "Improvement"
        TA = "Task"

    class STATUS_CHOICES(models.TextChoices):
        TD = "To Do"
        IP = "In progress"
        DO = "Donne"

    title = models.CharField(max_length=255, unique=True)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=70, choices=TAG_CHOICES.choices)
    priority = models.CharField(max_length=70, choices=PRIORITY_CHOICES.choices)
    project = models.ForeignKey(
        to=Projects,
        on_delete=models.CASCADE,
        related_name="issues"
    )
    status = models.CharField(max_length=70, choices=STATUS_CHOICES.choices)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="author"
    )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="assignee"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):

    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="comments"
    )
    issue = models.ForeignKey(
        to=Issues,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
