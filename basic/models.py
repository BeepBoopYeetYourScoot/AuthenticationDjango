from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # Это отображается только в базе данных


class Post(models.Model):  # Models are inherited from
    title = models.CharField(max_length=100)  # character field
    content = models.TextField()  # Content for the post
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade: delete post when the user is deleted; has 1 to many relationship

    def __str__(self):
        return self.title




