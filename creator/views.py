from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Creator
from .serializers import CreatorSerializer


class CreatorListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    pagination_class = None


class CreatorView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer


class TopCreatorView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Creator.objects.filter(top_creator=True)
    serializer_class = CreatorSerializer
    pagination_class = None
