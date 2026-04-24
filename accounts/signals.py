from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create additional user profile data if needed"""
    if created:
        # Здесь можно добавить дополнительные действия при создании пользователя
        # Например, отправку приветственного письма
        pass


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save user profile data"""
    pass
