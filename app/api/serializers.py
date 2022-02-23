from rest_framework import serializers
from ebooks.models import Ebook, Review


class EbookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ebook
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    ebook = EbookSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
