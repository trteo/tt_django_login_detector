import os

from django.contrib.auth import get_user_model
from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin_panel_login_detector.settings")

import django
django.setup()



MAILING_IMAGES_DIR = "static_content/mailing_images"
PRODUCT_IMAGES_DIR = "static_content/product_images"


User = get_user_model()


def create_superuser():
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin'

    # Check if the superuser already exists
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully.")
        except IntegrityError as e:
            print(f"Error creating superuser: {e}")
    else:
        print(f"Superuser '{username}' already exists.")


create_superuser()
