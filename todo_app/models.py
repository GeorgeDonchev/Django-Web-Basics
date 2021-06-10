from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.name}'


class Categories(models.Model):
    HOME = 'Home'
    LIFESTYLE = 'Lifestyle'
    PROGRAMMING = 'Programming'

    category_options = (
        (HOME, 'home'),
        (LIFESTYLE, 'lifestyle'),
        (PROGRAMMING, 'programming')
    )

    name = models.CharField(max_length = 30, choices = category_options)

    def __str__(self):
        return f'{self.name}'


class Todos(models.Model):
    DONE = 'Done'
    NOT_DONE = 'Not Done'
    options = [
        (DONE, 'Done'),
        (NOT_DONE, 'Not Done')
    ]
    subject = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    person = models.ForeignKey(Person, on_delete = models.CASCADE, default = 1)
    state = models.CharField(max_length = 10, choices = options, default = NOT_DONE)
    categories = models.ManyToManyField(Categories)

    def __str__(self):
        return f'{self.subject}'