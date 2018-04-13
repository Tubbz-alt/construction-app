from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Notification, CustomUser, UserNotification


@receiver(post_save, sender=Notification)
def save_user_notification(sender, instance, created, **kwargs):
    instance.notify_followers()
