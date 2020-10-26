from django.db import models

class Product(models.Model):
    CATEGORY = (
        ('Телефон','Телефон'),
        ('Компьютер','Компьютер'),
        ('Компьютер','Компьютер'),
        ('Жесткий диск','Жесткий диск'),
    )
    name = models.CharField(max_length=50,null=True)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    decsription = models.CharField(max_length=50,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name






