from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Ebook(models.Model):

    title = models.CharField(max_length=122)
    author = models.CharField(max_length=122)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)
    review = models.TextField(blank=True)
    rating = models.PositiveIntegerField(
        validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    ebook = models.ForeignKey(
        Ebook, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.review_author
