from django.db import models
from takpede.models import CustomUser

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    table_name = models.CharField(max_length=50)  # Jenis notifikasi, misal 'like', 'chat', dll.
    table_id = models.PositiveIntegerField()  # ID dari table (misal, id dari table 'like')
    message = models.TextField()  # Pesan notifikasi
    is_read = models.BooleanField(default=False)  # Status apakah sudah dibaca
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

