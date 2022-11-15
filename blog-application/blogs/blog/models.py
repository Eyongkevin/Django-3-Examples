from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from blogs.core.models import TimeStampedModel
from django.utils.functional import cached_property
from taggit.managers import TaggableManager
from django.db.models import Count

# Create your models here.


class PostManager(models.Manager):
    pass


class PostQuerySet(models.QuerySet):
    """Manage for Post model"""

    def published(self, **kwargs):
        """get all published posts"""
        return self.filter(status="pub", **kwargs)
        # return self.filter(publish__lte=timezone.now(), **kwargs)

    def author_by(self, author_id, **kwargs):
        return self.filter(author__id=author_id, **kwargs)

    def current_year_post(self, **kwargs):
        return self.filter(publish__year=timezone.now().year, **kwargs)


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
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.DRAFT,
        db_index=True,
    )

    objects = models.Manager()
    post = PostManager.from_queryset(PostQuerySet)()
    tags = TaggableManager()

    class Meta:
        """set Meta"""

        ordering = ("-publish",)

    @property
    def slug_source(self):
        """get blog's slug source"""

        return self.publish

    def __str__(self) -> str:
        return f"{self.title}"

    # @cached_property
    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

    def get_related_posts_by_tag(self):
        post_tag_ids = self.tags.values_list("id", flat=True)
        post_with_same_tags = Post.post.published(tags__in=post_tag_ids).exclude(
            id=self.id
        )
        post_with_same_tags = post_with_same_tags.annotate(
            same_tags=Count("tags")
        ).order_by("-same_tags", "-publish")[:4]

        return post_with_same_tags
