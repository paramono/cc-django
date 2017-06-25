from django.db import models


class TitleMixin(models.Model):
    title = models.CharField('Название', max_length=255)

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    position = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        abstract = True


class ActiveMixin(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    description = models.TextField('Описание', blank=True)

    class Meta:
        abstract = True


class ShortDescriptionMixin(models.Model):
    short_description = models.TextField('Краткое описание', blank=True)

    class Meta:
        abstract = True
