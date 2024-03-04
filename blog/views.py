from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import Post, Comment
# , Like
from .forms import CommentForm
from django.db.models import F
# from django.contrib.auth.decorators import login_required

# Create your views here.

class PostList(generic.ListView):
     queryset = Post.objects.filter(status=1)
     template_name = "blog/index.html"
     paginate_by = 3


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    like_count = post.like_count
    silly_count = post.like_count
    
    # like = False
    # if request.user.is_authenticated:
    #     if post.liked.filter(id=request.user.id).exists():
    #         like = True

    liked = False
    if post.liked.filter(id=request.user.id).exists():
        liked = True

    sillied = False
    if post.sillied.filter(id=request.user.id).exists():
        sillied = True
    

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
        "liked": liked,
        "like_count": like_count,
        "sillied": sillied,
        "silly_count": silly_count,
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


class PostVote(generic.RedirectView):
    """
    The PostVote view handles voting on posts.
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        vote_preference = request.POST.get('vote_preference')

        # Check the vote preference and handle accordingly
        if vote_preference == 'like':
            if post.liked.filter(id=request.user.id).exists():
                post.liked.remove(request.user)
                post.like_count -= 1
            else:
                post.liked.add(request.user)
                post.like_count += 1
                if post.sillied.filter(id=request.user.id).exists():
                    post.sillied.remove(request.user)
                    post.silly_count -= 1
                if post.more.filter(id=request.user.id).exists():
                    post.more.remove(request.user)
                    post.more_count -= 1
        elif vote_preference == 'silly':
            if post.sillied.filter(id=request.user.id).exists():
                post.sillied.remove(request.user)
                post.silly_count -= 1
            else:
                post.sillied.add(request.user)
                post.silly_count += 1
                if post.liked.filter(id=request.user.id).exists():
                    post.liked.remove(request.user)
                    post.like_count -= 1
                if post.more.filter(id=request.user.id).exists():
                    post.more.remove(request.user)
                    post.more_count -= 1
        elif vote_preference == 'moreinfo':
            if post.more.filter(id=request.user.id).exists():
                post.more.remove(request.user)
                post.more_count -= 1
            else:
                post.more.add(request.user)
                post.more_count += 1
                if post.liked.filter(id=request.user.id).exists():
                    post.liked.remove(request.user)
                    post.like_count -= 1
                if post.sillied.filter(id=request.user.id).exists():
                    post.sillied.remove(request.user)
                    post.silly_count -= 1
        post.save()
        return redirect('post_detail', slug=post.slug)