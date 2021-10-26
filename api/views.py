from rest_framework.viewsets import ModelViewSet
 
from posts.models import Post
from .serializers import PostSerializer
 
class PostViewset(ModelViewSet):
 
    serializer_class = PostSerializer
 
    def get_queryset(self):
        return Post.objects.all()