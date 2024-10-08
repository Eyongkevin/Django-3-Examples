import re
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import markdown
from blogs.blog.models import Post

register = template.Library()

DAYS_PER_YEAR = 365
DAYS_PER_MONTH = 30
DAYS_PER_WEEK = 7

MEDIA_CLOSED_TAGS = "|".join(["figure", "object", "video", "audio", "iframe"])
MEDIA_SINGLE_TAGS = "|".join(["img", "embed"])
MEDIA_TAGS_REGEX = re.compile(
    r"<(?P<tag>"
    + MEDIA_CLOSED_TAGS
    + ")[\S\s]+?</(?P=tag)>|"
    + r"<("
    + MEDIA_SINGLE_TAGS
    + ")[^>]+>",
    re.MULTILINE,
)


""" Tags """


@register.simple_tag
def total_posts():
    return Post.post.published().count()


@register.inclusion_tag("includes/list_posts_link.html")
def list_latest_posts(count):
    latest_posts = Post.post.published().order_by("-publish")[:count]
    return {"posts": latest_posts}


@register.simple_tag
def get_most_commented_posts(count):
    return (
        Post.post.published()
        .annotate(comment_count=Count("comments"))
        .order_by("-comment_count")[:count]
    )


""" Filters """


@register.filter(name="markdown")
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.filter(is_safe=True)
def date_since(specific_date):
    today = timezone.now()
    #  if isinstance(specific_date, datetime):
    #      specific_date = specific_date.date()
    diff = today - specific_date
    diff_years = int(diff.days / DAYS_PER_YEAR)
    diff_months = int(diff.days / DAYS_PER_MONTH)
    diff_weeks = int(diff.days / DAYS_PER_WEEK)
    diff_map = [
        ("year", "years", diff_years),
        ("month", "months", diff_months),
        ("week", "weeks", diff_weeks),
        ("day", "days", diff.days),
    ]
    for parts in diff_map:
        (interval, intervals, count) = parts
        if count > 1:
            return _(f"{count} {intervals} ago")
        elif count == 1:
            return _("yesterday") if interval == "day" else _(f"last {interval}")
    if diff.days == 0:
        seconds = diff.seconds
        minutes = seconds // 60 if seconds >= 60 else None
        hour = minutes // 60 if minutes >= 60 else None

        if not minutes:
            return _(f"{seconds} secs ago")
        if not hour:
            return _(f"{minutes} mins ago")

        return _(f"{hour} hrs ago")

    else:
        return f"{specific_date: %B %d, %Y}"


@register.filter
def first_media(content):
    tag_match = MEDIA_TAGS_REGEX.search(content)
    media_tag = ""
    if tag_match:
        media_tag = tag_match.group()
    return mark_safe(media_tag)


@register.filter
def humanize_url(url, letter_count=40):
    letter_count = int(letter_count)
    re_start = re.compile(r"^https?://")
    re_end = re.compile(r"/$")
    url = re_end.sub("", re_start.sub("", url))
    if len(url) > letter_count:
        url = f"{url[:letter_count - 1]}..."
    return url
