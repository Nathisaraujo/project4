from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import Post, Comment, Like
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
     queryset = Post.objects.filter(status=1)
     template_name = "blog/index.html"
     paginate_by = 9


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    like = False
    if request.user.is_authenticated:
        if post.liked.filter(id=request.user.id).exists():
            like = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "like": like,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def like_post(request, slug):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        if post.liked.filter(id=request.user.id).exists():
            post.liked.remove(request.user)
            like_count = post.liked.count()
            return JsonResponse({'liked': False, 'like_count': like_count})
        else:
            post.liked.add(request.user)
            like_count = post.liked.count()
            return JsonResponse({'liked': True, 'like_count': like_count})
    else:
        # return Httpg hnResponseRedirect(reverse('post_detail', args=[slug]))
        return JsonResponse({'error': 'Method not allowed'}, status=405)
