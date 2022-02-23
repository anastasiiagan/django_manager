from django.db import models
from django.core.validators import MinLengthValidator
#from django.core.validators import MinValueValidator, MaxValueValidator
#from django.utils.translation import gettext_lazy as _
#from django_extensions.db.models import TitleSlugDescriptionModel, TitleDescriptionModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Publication(models.Model):
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, default=None, related_name="publications")
    title = models.CharField( max_length=50)
    content = models.TextField(validators=[MinLengthValidator(50)])
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    #comment

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField( max_length=50)
    surname = models.CharField( max_length=50)
    #publication = models.ForeignKey('Publication', on_delete=models.SET_NULL, null=True, related_name="uclientr")