from django.db import models
from django.utils.translation import gettext_lazy as _
from blogs.blog.models import Post
from blogs.core.models import TimeStampedModel

# Create your models here.
class Comment(TimeStampedModel):
    post = models.ForeignKey(
        Post, verbose_name=_("post"), on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(_("name"), max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
