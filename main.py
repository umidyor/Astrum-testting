import os
import django
#
# # Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#
# # Initialize Django settings
django.setup()
#
# # Now you can import and use your models
from django.contrib.auth.models import User

# username = "Qodir"
# password = "qodirjon12"
#
# # Check if the user exists in the Regsiter_site model
# user_exists = Regsiter_site.objects.filter(username=username, password=password).exists()
# if user_exists:
#     print("Bor")
# else:
#     print("Yo'q")

import secrets

# Generate a random token of a specified length
# def generate_random_token(length):
#     # Generate a random byte string
#     random_bytes = secrets.token_bytes(length)
#
#     # Convert the random byte string to a hexadecimal representation
#     random_token = secrets.token_hex(length)
#
#     return random_token
#
# # Usage example: Generate a random token of length 32
# random_token = generate_random_token(32)
# print("Random Token:", random_token)

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

try:
    user = User.objects.get(username="Jamandar")
    user_id = user.password
    # user_id="Samandar_131415"
    # user.save()# This is the user's primary key (ID)
    print(user_id)
except ObjectDoesNotExist:
    # Handle the case when the user with the provided email doesn't exist
    print("yoq")
# email="Jalol"
# a=User.objects.get(username=email)
# print(a.email)

from blogs.models import Post
# def get_title():
#     return Post.objects.title
#
# print(get_title())