# Generated by Django 4.2 on 2024-03-06 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('image', models.ImageField(upload_to='brand', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('flag', models.CharField(choices=[('new', 'new'), ('sale', 'sale'), ('feature', 'feature')], max_length=10, verbose_name='Flag')),
                ('sku', models.CharField(max_length=12, verbose_name='Sku')),
                ('subtitle', models.CharField(max_length=120, verbose_name='Subtitle')),
                ('description', models.TextField(max_length=40000, verbose_name='Description')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_brand', to='product.brand', verbose_name='Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(verbose_name='Rate')),
                ('review', models.CharField(max_length=250, verbose_name='Review')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created_at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.product', verbose_name='Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images', verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='Product')),
            ],
        ),
    ]
