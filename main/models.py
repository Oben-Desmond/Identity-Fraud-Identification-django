from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Item (models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE) 
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__ (self) -> str:
        return self.text

# user model
class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200) 
    id_front= models.CharField(max_length=400)
    id_back= models.CharField(max_length=400)
    phone= models.CharField(max_length=200)
    lat= models.CharField(max_length=200)
    lng= models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    country= models.CharField(max_length=200)
    photo= models.CharField(max_length=400)

    # def __str__(self) -> str:
    #     return str({self.name, self.email, self.password, self.created_at,  self.phone, self.lat, self.lng, self.city, self.country, self.photo})


class AppTransactions(models.Model): 
    amount = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200) 
    sender_id = models.CharField(max_length=200)
    receiver_id = models.CharField(max_length=200)
    ref = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sender_photo = models.CharField(max_length=200)
    receiver_photo = models.CharField(max_length=200)
    sender_name = models.CharField(max_length=200)
    receiver_name = models.CharField(max_length=200)

    # def __str__(self) -> str:
    #     return str({ self.amount, self.created_at,  self.id, self.sender_id, self.receiver_id, self.ref, self.type, self.category,  self.sender_name, self.receiver_name})