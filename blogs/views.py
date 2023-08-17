from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm  # Import the form class

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Post


@login_required
def user_profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user)
    context = {
        'user_posts': user_posts,
    }

    return render(request, 'user_profile.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = request.POST['title']  # Access the title value using request.POST
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog.html', context)



def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'view_post.html', {'post': post})