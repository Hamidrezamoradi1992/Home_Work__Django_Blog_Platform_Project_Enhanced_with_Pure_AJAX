from rest_framework.serializers import ModelSerializer

from blog.models import Post, Author


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','description','id']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
