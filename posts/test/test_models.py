"""
We test the model POST  using the special function __str__
"""

import pytest

from django.test import Client
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

@pytest.mark.django_db  
def test_post_model():
    client = Client()
   
    post = Post()  
    post.title = 'title for test'
    post.created_at = timezone.now()
    post.body = "body for test"

    u = User(username = 'djonga')
    u.save()
    post.author = u 
    post.save()    

    expected_value = "djonga | title for test"
    assert str(post) == expected_value