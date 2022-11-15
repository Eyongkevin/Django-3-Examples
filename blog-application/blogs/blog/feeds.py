from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog"
    link = reverse_lazy("blog:post_view")
    description = "My latest blog posts"

    def items(self):
        return Post.post.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(item.body, 30)
