# Generated by Django 4.2 on 2023-05-06 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
