from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length= 10)
    address = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
