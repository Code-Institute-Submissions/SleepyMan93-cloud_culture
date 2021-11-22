from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderPerItem


@receiver(post_save, sender=OrderPerItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderPerItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on peritem delete
    """
    print('delete signal recieved!')
    instance.order.update_total()


