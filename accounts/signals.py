# accounts/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Esta función se ejecuta CADA VEZ que se guarda un objeto User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Si el usuario es nuevo, crea un perfil asociado
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Asegura que el perfil se guarde cuando el usuario se guarda
    instance.profile.save()