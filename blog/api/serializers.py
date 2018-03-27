from django.contrib.auth.models import User
from rest_framework.serializer import (
    ModelSerializer,
    HyperlinkedModelSerializer
)

from blog.models import BlogPost


class BlogpostListSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'author',
            'title',
            'updated'
        ]


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')
