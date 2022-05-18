from django.db import models

class Task(models.Model):
    """docstring for Task."""

    _id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    tag_id = models.IntegerField()
    name = models. CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    duedate = models.DateField()
    priority_list = (
    ( 'L' , 'Low'),
    ( 'M' , 'Middel'),
    ( 'H' , 'High'),
    )
    pariority = models.CharField (
        max_length = 1,
        choices = priority_list,
        default =  'M',
        )
    completed_at = models.DateField()
    Created_at =  models.DateField()
    updated_at =  models.DateField()
    deleted_at =  models.DateField()

class Group(models.Model):
    """docstring for Group."""
    _id = models.IntegerField(primary_key=True)
    name = models. CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    priority_list = (
    ( 'L' , 'Low'),
    ( 'M' , 'Middel'),
    ( 'H' , 'High'),
    )
    pariority = models.CharField (
        max_length = 1,
        choices = priority_list,
        default =  'M',
        )
    Created_at =  models.DateField()
    updated_at =  models.DateField()
    deleted_at =  models.DateField()

class Tag(models.Model):
    """docstring for Tag."""
    _id = models.IntegerField(primary_key=True)
    name = models. CharField(max_length = 255)
