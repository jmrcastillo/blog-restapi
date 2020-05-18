import pytest
from django.contrib.auth.models import User
from software.models import Blog


@pytest.fixture
def blog(db):
    """Test api url"""
    blog_post = Blog.objects.create(
        title="Test Jibreel Post", content="This is the content"
    )
    return blog_post


def test_blog_title(blog):
    name = Blog.objects.get(id=1)
    expected_title_name = f"{name.title}"
    assert "Test Jibreel Post" == expected_title_name


def test_blog_detail(blog):
    name = Blog.objects.get(id=1)
    expected_detail = f"{name.content}"
    assert "This is the content" == expected_detail
