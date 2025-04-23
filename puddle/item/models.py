from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# database model:

class category(models.Model):
    name=models.CharField(max_length=255)
    
    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'
        
    def __str__(self):
        return self.name

class Item(models.Model):
    category=models.ForeignKey(category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    description= models.TextField(blank=True, null=True)
    price=models.FloatField()
    image=models.ImageField(upload_to='item_images',blank=True, null=True)
    isSold=models.BooleanField(default=False)
    createdAt=models.DateTimeField(auto_now_add=True)
    createdBy=models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name