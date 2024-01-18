from django.conf import settings
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Video
from .forms import CommentForm


class IndexView(TemplateView):
    template_name = 'blog/index.html'


def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/posts.html', context)


from django.contrib.auth.models import User


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter()
    new_comment = True
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                new_comment.author = request.user
            else:
                anonymous_user = User.objects.get(username='Аноним')
                new_comment.author = anonymous_user
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, 'blog/post_details.html', context)



def videos(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, settings.VIDEOS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/videos.html', context)


def video_details(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        'video': video,
    }
    return render(request, 'blog/video_details.html', context)
