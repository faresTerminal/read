# Generated by Django 2.0.9 on 2020-05-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogArabic', '0003_auto_20200516_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=250),
        ),
    ]
