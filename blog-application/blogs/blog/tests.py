from django.test import TestCase
from blogs.blog.models import Post
import datetime


# Create your tests here.
class PostCreation(TestCase):
    def create_post(self):
        title = "Django"
        slug = "django"
        author = "Eyong"
        body = "This is a django application"
        # publish = "2023-02-06 14:53:44.176090"
        status = "pub"

        return Post.objects.create(
            title=title,
            slug=slug,
            author=author,
            body=body,
            status=status,
        )

    def test_post_creation(self):
        # Arrange
        post = self.create_post()

        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.title, "Django")
        self.assertTrue(isinstance(post.publish, datetime))

    def test_get_absolute_url(self):
        post = self.create_post()

        result = post.get_absolute_url()

        self.assertEqual(len(result.split("/")), 5),


# <int:year>/<int:month>/<int:day>/<slug:post>/
