from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from posts.models import Post


class PostSerializer(ModelSerializer):

    number_likes = serializers.IntegerField(source='likes.count', read_only=True)

    class Meta:
        model = Post
        fields = ['title' ,'body', 'created_at', 'number_likes'] 
