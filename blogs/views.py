from django.shortcuts import render,redirect
from .models import Post,Edd
from .forms import PostForm,PostSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponse,HttpResponseNotFound
from django.db import models
def login_required_decorator(f):
   return login_required(f,login_url="login")
@login_required_decorator
def user_profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user)
    context = {
        'user_posts': user_posts,
    }
    formsearch = PostSearchForm(request.GET)
    posts = Post.objects.filter(author=request.user)

    if formsearch.is_valid():
        query = formsearch.cleaned_data['query']
        if query:
            # Filter posts by title, author, or description containing the query
            posts = posts.filter(title__icontains=query) | \
                    posts.filter(description__icontains=query)

    return render(request, 'user_profile.html', {'user_posts': posts, 'form': formsearch})

@login_required_decorator
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = request.POST['title'].replace(" ","-").replace(",","").replace("'","").replace(".","")  # Access the title value using request.POST
            post.save()
            return redirect('profile')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog.html', context)



# @login_required_decorator
def view_post(request, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id,slug=post_slug)
    exist=Post.objects.filter(id=post_id,author=request.user).exists()
    if exist:
        return render(request, 'view_post.html', {'post': post})
    else:
        if request.POST:
            model=Edd()
            model.full_name=request.POST["full_name"]
            model.season=request.POST['season']
            model.phone_number=request.POST["phone_number"]
            model.post_id=post_id
            model.save()
            return HttpResponse("Siz so'rovnomani muvaffaqiyatli to'ldirdingiz.")
        return render(request,"edd_users.html",{'user_posts':[post]})


def much_posts_edd(request,post_slug):
    post = get_object_or_404(Post,slug=post_slug)
    post_id_inPost = Post.objects.get(slug=post.slug)
    edd = Edd.objects.filter(post_id=post_id_inPost.pk).exists()
    if edd:
        edd_ = Edd.objects.filter(post_id=post_id_inPost.pk)

        # print(edd.post_id)
        # print(edd.full_name)
        # print(edd.phone_number)
        # print(edd.season)
        return render(request,"much_posts_edd.html",{"post_any":edd_})
    else:
        return HttpResponse("Hali hech kim ushbu postga so'rovnoma to'ldirmadi😕")


def redirects_page(request):
    return render(request,"redirects.html")
def delete_post(request,post_id,post_slug):
    post=get_object_or_404(Post,id=post_id,slug=post_slug)
    exist=Post.objects.filter(id=post_id,author=request.user).exists()
    if exist:
        if post.delete():
            exist=Edd.objects.filter(post_id=post_id).exists()
            if exist:
                edds = Edd.objects.filter(post_id=post_id)
                for edd in edds:
                    edd.delete()
                return redirect('redirect_delete')
    else:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")
        # return HttpResponse("""Succsesfully deleted this post <a href="{% url 'login' %}"></a>""")
    return render(request,"redirects.html")





def edit_post(request, post_id, post_slug):
    post = Post.objects.get(id=post_id, slug=post_slug)
    exist = Post.objects.filter(id=post_id, slug=post_slug, author=request.user).exists()
    if exist:
        if request.method != 'POST':
            form = PostForm(instance=post)
        else:
            form = PostForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('profile')
        context = {'post': post, 'form': form}
        return render(request, 'edit_post.html', context)
    else:
        return HttpResponseNotFound("<h1>404 Not Found</h1>")



from django.http import FileResponse
from django.conf import settings
import os

def serve_media(request, file_path):
    # Build the absolute path to the requested media file
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file using FileResponse
        response = FileResponse(open(file_path, 'rb'))
        return response
    else:
        # Handle file not found gracefully
        print("asdasdasdas")


def share_post(request, post_id,post_slug):
    post_url = get_object_or_404(Post, id=post_id,slug=post_slug)
    return render(request, 'share_post.html', {'post_url': post_url})


# views.py






