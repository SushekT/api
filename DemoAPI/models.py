
# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

# Create your models here.
class Profile(models.Model):
    
    GENDER_OPT = (
        (('male'), ('Male')),
        (('female'), ('Female')),
        (('other'), ('Other')),
        ('', '')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    phone = models.PositiveIntegerField()
    gender = models.CharField(blank=True, max_length=10, choices=GENDER_OPT, null=True)
    date_created = models.DateTimeField(auto_now_add=True)