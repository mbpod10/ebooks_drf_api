# Ebooks API DRF
```py
# class EbookCreateListRetrieveViewSet(mixins.ListModelMixin,
#                                      mixins.CreateModelMixin,
#                                      generics.GenericAPIView):

#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
```