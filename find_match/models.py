from django.db import models
from takpede.models import CustomUser

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)

    def is_liked_by(self, user):
        return self.post_likes.filter(user=user).exists()

    def get_absolute_url(self):
        return reverse('find_match', args=[str(self.id)])

class Likes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

