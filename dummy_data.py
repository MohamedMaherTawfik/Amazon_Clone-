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
            image = f'brand/{images[random.randint(0,12)]}',
        )
    print(f'{n}:brands_made_sucessfully')

#======================================
def seed_product(n):
    fake=Faker()
    images=['samsung-logo.jpeg','Apple.jpeg','1.jpeg','2.jpeg','3.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','Apple.jpeg','images.jpeg']
    flags=['new','sale','feature']
    for _ in range(n):
        Product.objects.create(
            name = fake.name(),
            image = f'brand/{images[random.randint(0,12)]}',
            flag=flags[random.randint(0,2)],
            sku=random.randint(130,15000),
            subtitle=fake.text(max_nb_chars=50),
            quantity=random.randint(0,30),
            price=round(random.uniform(20.99,99.99),2),
            description=fake.text(max_nb_chars=2000),
            brand = Brand.objects.get(id=random.randint(405,510)),
            )
    print(f'{n}:Products_made_sucessfully')


# seed_brand(120)
seed_product(2000)
