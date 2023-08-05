from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem
from django.contrib.auth.models import User


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):

    instance.order.update_total()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Wishlist.objects.create(user=instance.userprofile)

        """ Wishlist.objects.create(user=instance.userprofile) """
    instance.userprofile.save()