from rest_framework import generics
from .models import Gundam
from .serializers import GundamSerializer

class GundamListView(generics.ListAPIView):
    queryset = Gundam.objects.all()
    serializer_class = GundamSerializer
