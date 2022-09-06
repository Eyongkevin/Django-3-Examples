from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from blogs.core.models import TimeStampedModel

# Create your models here.


class PostManager(models.Manager):
    pass


class PostQuerySet(models.QuerySet):
    """Manage for Post model"""

    def published(self, **kwargs):
        """get all published posts"""
        return self.filter(publish__isnull=False, **kwargs)
        # return self.filter(publish__lte=timezone.now(), **kwargs)

    def author_by(self, author_id, **kwargs):
        return self.filter(author__id=author_id, **kwargs)


class Post(TimeStampedModel):
    """model for Post"""

    class StatusChoices(models.TextChoices):
        """Status choices"""

        PUBLISHED = "pub", "Published"
        DRAFT = "dra", "Draft"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.DRAFT
    )

    objects = models.Manager()
    post = PostManager.from_queryset(PostQuerySet)()

    class Meta:
        """set Meta"""

        ordering = ("-publish",)

    @property
    def slug_source(self):
        """get blog's slug source"""

        return self.publish

    def __str__(self) -> str:
        return f"{self.title}"
