from django.db import models
from djangogram.users import models as user_model

# Create your models here.
class TimeStamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='post_author'
            )
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.models.ManyToManyField(user_model.User, related_name=_("post_image_likes")

class Comment():
    author = models.ForeignKey(
                user_model.User, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='post_author'
            )
    posts = author = models.ForeignKey(
                Post, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='cpmment_post'
            )
    contents = models.TextField(blank=True)