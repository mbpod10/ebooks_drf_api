from rest_framework import generics
from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from ebooks.api.permissions import IsAdminUserOrReadOnly

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer


class EbookCreateListRetrieveViewSet(generics.ListCreateAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
