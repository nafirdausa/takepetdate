from django.db.models.signals import post_save
from django.dispatch import receiver
from takpede.models import CustomUser
from find_match.models import Post

@receiver(post_save, sender=CustomUser)
def create_post_for_user(sender, instance, created, **kwargs):
    if created:  # Hanya buat Post jika user baru dibuat
        Post.objects.create(user=instance, likes=0)
