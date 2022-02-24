from django.urls import path
from ebooks.api.views import EbookCreateListRetrieveViewSet, EbookDetailViewSet, \
    ReviewDetailAPIView, ReviewCreateAPIView

urlpatterns = [
    path('ebooks/', EbookCreateListRetrieveViewSet.as_view(),
         name='ebook-list'),

    path('ebooks/<int:pk>/',
         EbookDetailViewSet.as_view(), name='ebook-detail'),

    path('ebooks/<int:ebook_pk>/review/',
         ReviewCreateAPIView.as_view(), name='ebook-review'),

    path('reviews/<int:pk>/',
         ReviewDetailAPIView.as_view(), name='review-detail'),
]
