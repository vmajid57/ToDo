from django.db import models

class Task(models.Model):
    """docstring for Task."""

    _id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    tag_id = models.IntegerField()
    name = models. CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    duedate = models.DataField()
    priority_list = (
    ( L , 'Low'),
    ( M , 'Middel'),
    ( H , 'High'),
    )
    pariority = models.CharField (
        max_length = 1,
        choices = pariority_list,
        default =  M,
        )
    completed_at = models.DataField()
    Created_at =  models.DataField()
    updated_at =  models.DataField()
    deleted_at =  models.DataField()

class Group(models.Model):
    """docstring for Group."""
    _id = models.IntegerField(primary_key=True)
    name =models. CharField(max_length = 255)
    description = models.CharField(max_length = 500)
    priority_list = (
    ( L , 'Low'),
    ( M , 'Middel'),
    ( H , 'High'),
    )
    pariority = models.CharField (
        max_length = 1,
        choices = pariority_list,
        default =  M,
        )
    Created_at =  models.DataField()
    updated_at =  models.DataField()
    deleted_at =  models.DataField()

class Tag(models.Model):
    """docstring for Tag."""
    _id = models.IntegerField(primary_key=True)
    name =models. CharField(max_length = 255)
