from unicodedata import name
from django.db import models

# Create your models here.

class Food:
    id : int 
    name : str
    availableTime : str
    imgUrl: str
    ingred : list
    price : float
    calories : float
    isAvailable : bool
    rating = str

