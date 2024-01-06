import os
import django
#
# # Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# #
# # # Initialize Django settings
django.setup()
# #
# # # Now you can import and use your models
# from django.contrib.auth.models import User
#
# # username = "Qodir"
# # password = "qodirjon12"
# #
# # # Check if the user exists in the Regsiter_site model
# # user_exists = Regsiter_site.objects.filter(username=username, password=password).exists()
# # if user_exists:
# #     print("Bor")
# # else:
# #     print("Yo'q")
#
# import secrets
#
# # Generate a random token of a specified length
# # def generate_random_token(length):
# #     # Generate a random byte string
# #     random_bytes = secrets.token_bytes(length)
# #
# #     # Convert the random byte string to a hexadecimal representation
# #     random_token = secrets.token_hex(length)
# #
# #     return random_token
# #
# # # Usage example: Generate a random token of length 32
# # random_token = generate_random_token(32)
# # print("Random Token:", random_token)
#
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from blogs.models import Post,Edd
#
# id=13
# post_id_inPost=Post.objects.get(slug="Shaxmat-musobaqasi")
# edd=Edd.objects.filter(post_id=post_id_inPost.pk).exists()
# if edd:
#     edd = Edd.objects.filter(post_id=post_id_inPost.pk)
#     for i in edd:
#         print(i.full_name)
#     # print(edd.post_id)
#     # print(edd.full_name)
#     # print(edd.phone_number)
#     # print(edd.season)
#
# # try:
# #     user = User.objects.get(username="Jamandar")
# #     user_id = user.password
# #     # user_id="Samandar_131415"
# #     # user.save()# This is the user's primary key (ID)
# #     print(user_id)
# # except ObjectDoesNotExist:
# #     # Handle the case when the user with the provided email doesn't exist
# #     print("yoq")
# # email="Jalol"
# # a=User.objects.get(username=email)
# # print(a.email)
#
# from blogs.models import Post
# # def get_title():
# #     return Post.objects.title
# #
# # print(get_title())

from blogs.models import Cmodel
from django.shortcuts import get_object_or_404,get_list_or_404
# formset = Cmodel.objects.get(title="Osh").exists()
# if formset:
#     print(True)
# else:
#     print(False)

# import sqlite3
#
# con = sqlite3.connect("db.sqlite3")
# c = con.cursor()
# c.execute("SELECT content FROM blogs_cmodel WHERE slug_link='3/qweqweq/2023-11-28T09:58/5B6E9456ab87F1FA62Edd81C1e54aDf0a5313EBD'")
# result = c.fetchall()
# con.close()
#
# print(result)
from django.shortcuts import render,get_object_or_404
from blogs.models import NumQuest,Cmodel,ResponseModel
from django.contrib.auth.models import User
#
user_instance = User.objects.get(username='Umidyor')
# #
# related_numquests = NumQuest.objects.filter(author=user_instance)

# form = get_object_or_404(NumQuest, title="shamsho")
# for i in form:
#     print(i)
# title_instance=get_object_or_404(NumQuest,title="atabek")
# form=Cmodel.objects.filter(title=title_instance,author="Umidyor",date_quest="2023-12-27T14:21")
# for i in form:
#     print(i.content)

# form=ResponseModel.objects.filter(response_author=user_instance)
# for i in form:
#     s=str(i.response_title).split("^")
#     print(s[1])
#
# title_instance = get_object_or_404(NumQuest, title="salom")
# form_cmodel = Cmodel.objects.filter(title=title_instance, author="Umidyor", date_quest="2024-01-03T19:33")
# for form in form_cmodel:
#     print(form.title)
#
# title_instance_2=NumQuest.objects.get(title=title_instance)
# print(title_instance_2)

# author_instance=get_object_or_404(User,username="Umidyor")
# print(author_instance)
# title_instance = get_object_or_404(NumQuest, title="salom", time_quest="2024-01-03T19:33")
# print(title_instance)
# for_numquest_form=get_object_or_404(NumQuest,title="salom",author=user_instance)
# print(for_numquest_form)

from blogs.models import ResponseModel,NumQuest
user_instance = User.objects.get(username='Umidyor')
numquest_title=NumQuest.objects.get(title="Futbol musobaqasi",author=user_instance)
responses=ResponseModel.objects.filter(response_title=numquest_title,response_author=user_instance,response_date="2024-01-04 15:22:00+00:00")
table_column=Cmodel.objects.filter(title=numquest_title,date_quest="2024-01-04 15:22:00+00:00")
