from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Revisor(models.Model):
    texto = models.CharField(max_length=500)