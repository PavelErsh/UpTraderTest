from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Menu Name"))

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name="items", on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100, verbose_name=_("Item Name"))
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("URL"))
    named_url = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Named URL")
    )
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url
