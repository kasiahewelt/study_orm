from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    available = models.BooleanField(deafult=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name




if __name__ == '__main__':