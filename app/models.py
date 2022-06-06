from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)

    class Meta:
        db_table = 'posts'
