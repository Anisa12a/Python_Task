from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Task(models.Model):
    task_id = models.CharField(primary_key=True, max_length=20, db_column='task_id')
    task_name = models.CharField(max_length=20)
    task_description = models.TextField(max_length=50)
    task_start_date = models.DateField()
    task_due_date = models.DateField()
    task_status = models.TextField(max_length=20)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE) 