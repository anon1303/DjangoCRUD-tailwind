from django.db import models

# Create your models here.
class ListMovies(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(  max_length=100)


# makemigrations
# # creates instructions telling django how the db change

# migrate
# # applies the changes