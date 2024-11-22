from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.contrib.postgres.fields import ArrayField
from  django.core.validators import MinValueValidator,MaxValueValidator
import uuid
from django.contrib import admin

class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance, filename)

class Person(models.Model):
    # class Gender(models.TextChoices):
    #     MALE = 'M', _('Male')
    #     FEMALE = 'F', _('Female')
    #     OTHERS = 'O', _('Others')
   
   

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE
    )
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField(max_length=250, null=True, validators=[validate_email])
    picture = models.FileField(upload_to=user_directory_path, null=True)

    


    def __str__(self):
        return self.name




class Cnic(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT, blank=False)
    number = models.CharField(max_length=20, null=False)
    expiry_data = models.DateField()


    def __str__(self) -> str:
        return self.number
    
 

class Projects(models.Model):
    assigne = models.ForeignKey(Person, on_delete=models.CASCADE , related_name="person")
    project_name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=250, null=True)
    tech =   ArrayField(models.CharField(max_length=10, null=False))

    def __str__(self) -> str:
        return self.project_name
    





class Customer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    customer_name = models.ManyToManyField(Customer)

    def __str__(self):
        return self.product_name







class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, through='Authorship')

    def __str__(self):
        return self.title


class Authorship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)                       
    contribution_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def get_author_role(self):
        return self.role

    def __str__(self):
        return f"{self.author.name} ({self.role}) for {self.book.title}"
    


        

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

class Car(Vehicle):
    number_of_doors = models.IntegerField()

    def __str__(self) -> str:
        return self.make
    



class Student(models.Model):
    name = models.CharField(max_length=20, null=False)
    subject = models.CharField(max_length=20, null=False)
    roll_no = models.CharField(max_length=20, null=False)
    session = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return f"{self.name} {self.subject} {self.roll_no}"
    


class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    userName = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name} {self.email}"






class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=15, null=False)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, null=False)
    rating = models.DecimalField(
        max_digits=4, 
        decimal_places=1, 
        validators=[
            MinValueValidator(1.0),  
            MaxValueValidator(10.0)
        ]
    )
    genre = models.ManyToManyField(Genre)

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = "Genre"

    @admin.display(boolean=True, ordering="movie",description="Super Movie")
    def best_movie(self):
        return self.rating > 8.4

    def __str__(self):
        return self.name
