from django.db import models
from takpede.models import CustomUser

# Create your models here.
class Likers(models.Model):
    # pengguna yang mendapatkan like.
    user_id = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="liked_by"  # Untuk membedakan relasi jika ada ForeignKey lain
    )
    # pengguna yang memberikan like.
    liker_id = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name="likers"  # Memberikan nama relasi unik untuk FK kedua
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp kapan "like" dibuat

    def __str__(self):
        return f"{self.liker.username} liked {self.user.username}"
