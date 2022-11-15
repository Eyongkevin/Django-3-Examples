from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    TrigramSimilarity,
)
from .models import Post
from blogs.comment.models import Comment
from blogs.comment.forms import CommentForm
from . import mixins
from .form import EmailPostForm, SearchForm
from blogs.core.utils import admin_required, check_if_admin
from django.conf import settings
from taggit.models import Tag
from .utils import search_filter

# Create your views here.


class PrimeView(LoginRequiredMixin, mixins.PrimeMixin, TemplateView):
    template_name: str = "blog/prime.html"


class PostListView(LoginRequiredMixin, mixins.SearchMixin, ListView):
    # model = Post # This without the queryset will apply 'Post.objects.all()``
    queryset = Post.post.published()
    context_object_name = "posts"  # object_list by default
    paginate_by: int = 2
    template_name = (
        "blog/post/list.html"  # it will look for post_list.html in templates by default
    )


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "slug", "author", "body", "status"]


@login_required
def post_list(request, tag_slug=None):
    # request = check_if_admin(request)
    object_list: Post = Post.post.published()
    object_list = search_filter(request, object_list)

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    posts = mixins.pagination(request, object_list)
    return render(request, "blog/post/list.html", {"posts": posts, "tag": tag})


@admin_required
def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    shared_posts = post.get_related_posts_by_tag()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "shared_posts": shared_posts,
        },
    )


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="pub")
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url)
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}'s comments: {cd['comments']}"
            )
            send_mail(subject, message, settings.EMAIL_ADDRESS, [cd["to"]])
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request, "blog/post/share.html", {"post": post, "form": form, "sent": sent}
    )


def post_search(request):
    query = None
    form = SearchForm()
    results = []
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            # search_vector = SearchVector("title", weight="A") + SearchVector(
            #     "body", weight="B"
            # )
            search_vector = SearchVector("title", "body")
            search_query = SearchQuery(query)
            results = (
                Post.objects.annotate(
                    # rank=SearchRank(search_vector, search_query)
                    similarity=TrigramSimilarity("title", query)
                )
                .filter(similarity__gte=0.1)
                .order_by("-similarity")
            )
    return render(
        request,
        "blog/post/searchme.html",
        {"form": form, "query": query, "results": results},
    )
