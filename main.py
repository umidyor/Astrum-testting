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
from register.models import Regsiter_site

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

a=Regsiter_site.objects.get(email="umidyor007@gmail.com")
print(a.pk)