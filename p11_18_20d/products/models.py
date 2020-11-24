from django.db import models
from django.urls import reverse
# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=1000)
    summary=models.TextField()

class Rproduct(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    email = models.EmailField()
    price = models.DecimalField(decimal_places=2,max_digits=1000)

    def get_absolute_url(self):
        return f"/products/{self.id}/"                                      #        return reverse("product:rproduct",kwargs={"id":id})