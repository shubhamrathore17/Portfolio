from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

        
    class Meta:
        abstract = True

class Profile(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    background = models.CharField(max_length=50, blank=True,  null=True)
    about_featured = models.TextField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    live_in = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pictures')
