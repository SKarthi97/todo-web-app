from django.db import models
from django.urls import reverse

from django.utils import timezone


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("list", args=[self.id])


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    def get_absolute_url(self):
        return reverse("item_update", args={str(self.todo_list.id), str(self.id)})
