# Generated by Django 4.0.2 on 2022-02-23 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_in_inglish', models.CharField(max_length=200, unique=True, verbose_name='اسم المنتج بالانجليزي')),
                ('product_name_in_arabic', models.CharField(max_length=200, unique=True, verbose_name='اسم المنتج بالعربي')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='اسم المنتج في الرابط')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='الوصف')),
                ('price', models.IntegerField(verbose_name='السعر')),
                ('images', models.ImageField(upload_to='photos/products', verbose_name='الصوره')),
                ('is_available', models.BooleanField(default=True, verbose_name='متوفر؟')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الأضافه')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='اخر تعديل')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
