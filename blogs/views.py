from django.shortcuts import render,redirect
from .models import Post,Edd,Cmodel,NumQuest,ResponseModel
from .forms import PostForm,PostSearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
from .generation_slug import generate_secure_slug
from django.contrib.auth.models import User

from django.contrib import messages

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
        unique_slug = str(uuid.uuid4())[:20]  # Generate a UUID and truncate it to 20 characters
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Generate a unique slug for the post based on the title
            post_slug = request.POST['title'].replace(" ","-").replace(",","").replace("'","").replace(".","").replace('[',"").replace("]","").replace(":","").replace(";","")
            shared_slug = slugify(post.title + '-' + unique_slug)
            post.slug = f'{post_slug}-{shared_slug}'  # Combine the post slug and shared slug
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
        print("Error image serve_media")

import uuid
from django.utils.text import slugify
def share_post(request, post_id,post_slug):
    post_url = get_object_or_404(Post, id=post_id,slug=post_slug)
    return render(request, 'share_post.html', {'post_url': post_url})




from .forms import CKEditorForm,NumQuestForm

"""NEED OTHER CODE"""
# @login_required_decorator
# def create_editor_view(request, author,cmid, num_quest, title, time_quest, slug):
#     if author==request.user.username:
#         nqm = NumQuest.objects.get(pk=cmid)
#         user_instance = User.objects.get(username=author)
#         cmodels = nqm.Num_quests.all()
#         if request.method == 'POST':
#             cmodelforms = [
#                 CKEditorForm(request.POST,  instance=cmodel, prefix=f'option_{cmodel.id}')
#                 for cmodel in cmodels
#             ]
#             if all([form.is_valid() for form in cmodelforms]):
#                 for form in cmodelforms:
#                     form.save()
#             return redirect("listforms")
#         cmodelforms = [
#             CKEditorForm(instance=cmodel, prefix=f'option_{cmodel.id}')
#             for cmodel in cmodels
#         ]
#     else:
#         return HttpResponse("404 ga o'tkaz esdan chiqmasin.")
#
#
#     return render(request, 'create_editor.html',
#                   {'cmodels':cmodelforms})

@login_required_decorator
def create_editor_view(request, author, cmid,num_quest, title, time_quest, slug):
    if author == request.user.username:
        nqm = get_object_or_404(NumQuest, pk=cmid)
        cmodels = nqm.Num_quests.all()

        if request.method == 'POST':
            num_quest_form = NumQuestForm(request.POST, instance=nqm)
            if num_quest_form.is_valid():
                # Check if a NumQuest instance with the same title already exists
                # existing_num_quest = NumQuest.objects.filter(title=num_quest_form.cleaned_data['title']).exclude(pk=cmid).first()
                # if existing_num_quest:
                #     # context = {
                #     #     'error': 1
                #     # }
                #     messages.warning(request, "This 'title' is already written.Make any letter lowercase or uppercase to keep the same title!")
                #     return redirect("create_editor", author=author, cmid=cmid, num_quest=num_quest,
                #                     title=title, time_quest=time_quest, slug=slug)


                num_quest_form.save()

            cmodelforms = [
                CKEditorForm(request.POST, instance=cmodel, prefix=f'option_{cmodel.id}')
                for cmodel in cmodels
            ]

            if all([form.is_valid() for form in cmodelforms]):
                for form in cmodelforms:
                    form.save()
                return redirect("listforms")

        else:
            num_quest_form = NumQuestForm(instance=nqm)

        cmodelforms = [
            CKEditorForm(instance=cmodel, prefix=f'option_{cmodel.id}')
            for cmodel in cmodels
        ]
    else:
        return HttpResponse("404 ga o'tkaz esdan chiqmasin.")

    return render(request, 'create_editor.html', {'cmodels': cmodelforms, 'num_quest_form': num_quest_form})








@login_required_decorator
def list_forms(request):
    user_instance = User.objects.get(username=request.user)
    related_numquests = NumQuest.objects.filter(author=user_instance)
    return render(request,"custom_ckeditor/form_lists.html",{'related_numquests':related_numquests})

"""NEDD OTHER CODES"""

# @login_required_decorator
# def range_numb(request):
#     if request.method == 'POST':
#         num_quest = int(request.POST["num_quest"])
#         title = request.POST["title"]
#         time_quest = request.POST["time_quest"]
#         author=request.user
#         slug = generate_secure_slug(title)
#
#         author_instance = get_object_or_404(User, username=author)
#
#         check_title_use_author=NumQuest.objects.filter(author=author_instance,title=title).exists()
#         if check_title_use_author==False:
#             num_quest_instance = NumQuest(
#                 title=title,
#                 description=request.POST["description"],
#                 num_quest=num_quest,
#                 time_quest=time_quest,
#                 author=author,
#             )
#             num_quest_instance.save()
#         else:
#             return HttpResponse(f"<h1>This '{title}' has your blogs.Rewrite other title!Please<a href='number_quest'>try again🤏</a></h1>")
#
#         slug_url = f"http://127.0.0.1:8000/create_editor/{author}/{num_quest_instance.id}/{num_quest}/{title}/{time_quest}/{slug}/edit"
#         # Create num_quest instances in Cmodel with the same title and time_quest
#         for i in range(num_quest):
#             model = Cmodel.objects.create(
#                 title=num_quest_instance,
#                 date_quest=time_quest,
#                 author=author,
#                 slug_link=slug_url
#             )
#         return redirect("create_editor", author=author, cmid=num_quest_instance.id, num_quest=num_quest, title=title, time_quest=time_quest, slug=slug)
#     return render(request, "custom_ckeditor/form_range.html")




from django.template import loader
@login_required_decorator
def range_numb(request):
    num_quest_instance = None  # Initialize num_quest_instance outside the if block
    if request.method == 'POST':
        num_quest = int(request.POST["num_quest"])
        title = request.POST["title"]
        time_quest = request.POST["time_quest"]
        author = request.user
        slug = generate_secure_slug(title)

        author_instance = get_object_or_404(User, username=author)

        check_title_use_author = NumQuest.objects.filter(author=author_instance, title=title).exists()
        if check_title_use_author == False:
            num_quest_instance = NumQuest(
                title=title,
                description=request.POST["description"],
                num_quest=num_quest,
                time_quest=time_quest,
                author=author,
            )
            num_quest_instance.save()
        else:
            template = loader.get_template('custom_ckeditor/form_range.html')
            context = {
                'error': 1
            }
            return HttpResponse(template.render(context, request))

        slug_url = f"http://127.0.0.1:8000/create_editor/{author}/{num_quest_instance.id}/{num_quest}/{title}/{time_quest}/{slug}/edit"
        # Create num_quest instances in Cmodel with the same title and time_quest
        for i in range(num_quest):
            model = Cmodel.objects.create(
                title=num_quest_instance,
                date_quest=time_quest,
                author=request.user,
                cmid=num_quest_instance.id,
                slug_link=slug_url
            )
        return redirect("create_editor", author=author, cmid=num_quest_instance.id, num_quest=num_quest,
                        title=title, time_quest=time_quest, slug=slug)
    return render(request, "custom_ckeditor/form_range.html")




def use_title(request, title, author, date_quest):
    author_instance = get_object_or_404(User, username=author)
    title_instance = get_object_or_404(NumQuest, title=title,time_quest=date_quest)
    form_cmodel = Cmodel.objects.filter(title=title_instance, author=author_instance, date_quest=date_quest)
    title_instance_2 = NumQuest.objects.get(title=title_instance, author=author_instance)
    if request.method == 'POST':
        for form in form_cmodel:
            response_text = request.POST.get(str(form.pk))
            response_instance = ResponseModel(
                response_text=response_text,
                response_title=title_instance_2,
                response_author=author_instance,
                response_date=date_quest,
            )
            response_instance.save()
        if request.user.username==author:
            return redirect("listforms")
        return HttpResponse("Sizning so'rovnoma javoblaringiz qabul qilindi!")

    return render(request, "custom_ckeditor/use_title.html", {'form_cmodel': form_cmodel,'tit_dec':title_instance_2})




########
@login_required_decorator
def result(request,title,author,date):
    user_instance = User.objects.get(username=author)
    numquest_title = NumQuest.objects.get(title=title, author=user_instance)
    responses = ResponseModel.objects.filter(response_title=numquest_title, response_author=user_instance,response_date=date)
    table_column = Cmodel.objects.filter(title=numquest_title, date_quest=date)
    grouped_data = group_list(responses, len(table_column))

    return render(request,"custom_ckeditor/results.html",{'responses':grouped_data,'table_column':table_column})


def share_anketa(request,title,author,date):
    user_instance = User.objects.get(username=author)
    anketa=get_object_or_404(NumQuest,title=title,author=user_instance,time_quest=date)
    return render(request,"share_anketa.html",{'anketa_url':anketa})


def delete_anketa(request,title,author,date):
    user_instance = User.objects.get(username=author)
    anketa_delete = get_object_or_404(NumQuest, title=title, author=user_instance, time_quest=date)
    anketa_delete.delete()
    return redirect("listforms")
def group_list(data_list, group_size):
    return [data_list[i:i+group_size] for i in range(0, len(data_list), group_size)]



# from rest_framework.response import Response
# from rest_framework import views,status
# class TitleAPIView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         title = request.data.get('title')
#         num_quest = request.data.get("num_quest")
#         description = request.data.get("description")
#         time_quest = request.data.get("time_quest")
#         author = request.user
#         slug = generate_secure_slug(title)
#
#         author_instance = get_object_or_404(User, username=author)
#
#         check_title_use_author = NumQuest.objects.filter(author=author_instance, title=title).exists()
#         if title is not None:
#             if check_title_use_author:
#                 return Response({'message': "Duplicate title"}, status=status.HTTP_400_BAD_REQUEST)
#
#             num_quest_instance = NumQuest(
#                 title=title,
#                 description=description,
#                 num_quest=num_quest,
#                 time_quest=time_quest,
#                 author=author,
#             )
#             num_quest_instance.save()
#             slug_url = f"http://127.0.0.1:8000/create_editor/{author}/{num_quest_instance.id}/{num_quest}/{title}/{time_quest}/{slug}/edit"
#             for i in range(int(num_quest)):
#                 model = Cmodel.objects.create(
#                     title=num_quest_instance,
#                     date_quest=time_quest,
#                     author=request.user,
#                     cmid=num_quest_instance.id,
#                     slug_link=slug_url
#                 )
#
#         redirect_url = f"create_editor/{author}/{num_quest_instance.id}/{num_quest}/{title}/{time_quest}/{slug}/edit"
#         return Response({"redirect_url": redirect_url}, status=status.HTTP_200_OK)

        # return Response({'message': "Title is None or not provided"}, status=status.HTTP_400_BAD_REQUEST)