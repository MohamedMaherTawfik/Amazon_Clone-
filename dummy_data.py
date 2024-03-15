import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from product.models import Brand,Product


def seed_brand(n):
    fake=Faker()
    images=['samsung-logo.jpeg','Apple.jpeg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','Apple.jpeg','images.jpeg']
    for _ in range(n):
        Brand.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(0,11)]}',
        )
    print(f'{n}:brands_made_sucessfully')


def seed_product(n):
    pass


seed_brand(120)
# seed_product(0)
# 