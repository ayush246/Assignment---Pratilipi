from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    reads_current=models.IntegerField(default=0)
    reads_total=models.IntegerField(default=0)
    user_current = models.ForeignKey(User,on_delete=models.CASCADE)
    def summary(self):
        return self.body[:100]
    def __str__(self):
        return self.title

    @property
    def viewCount(self):
        return PostView.objects.filter(product=self).count()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    def str(self):
        return self.user.username