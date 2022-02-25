from rest_framework import serializers
from ebooks.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField()

    class Meta:
        model = Review
        exclude = ('ebook',)


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    no_of_reviews = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Ebook
        fields = '__all__'

    def get_no_of_reviews(self, object):
        reviews = Review.objects.filter(ebook=object)
        return len(reviews)

    def get_avg_rating(self, object):
        sum = 0
        reviews = Review.objects.filter(ebook=object)
        for review in reviews:
            sum = sum + review.rating
        if len(reviews) > 0:
            return sum / len(reviews)
        else:
            return 0
