"""
We test that the url and the correspondind view are correct
"""

import pytest

from django.urls import reverse, resolve
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

@pytest.mark.django_db    
def test_post_url():
    post = Post()  
    post.title = 'title for test'
    post.created_at = timezone.now()
    post.body = "body for test"

    u = User(username = 'djonga')
    u.save()
    post.author = u 
    post.save()

    path = reverse('post_detail', kwargs={'pk':1})
    
    assert path == "/post/1/"
    assert resolve(path).view_name == "post_detail"