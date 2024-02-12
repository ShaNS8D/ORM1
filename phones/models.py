from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Phone(models.Model):
    name = models.CharField(max_length=53)
    slug = models.SlugField(blank=True, unique=True, db_index=True, verbose_name='URL')
    price =models.IntegerField()
    image = models.CharField(max_length=255)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)

    # def __str__(self) -> str:
    #         return self.title
    
@receiver(pre_save, sender=Phone)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)