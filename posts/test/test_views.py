"""
We verify the http response is valid for a created post in detail view
"""

import pytest

from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post

@pytest.mark.django_db  
def test_post_infos_view():
    client = Client()

    post = Post()  
    post.title = 'title for test'
    post.created_at = timezone.now()
    post.body = "body for test"
    u = User(username = 'djonga')
    u.save()
    post.author = u 
    post.save()
    
    path = reverse('post_detail', kwargs={'pk':post.id})
    response = client.get(path)
   
    assert response.status_code == 200