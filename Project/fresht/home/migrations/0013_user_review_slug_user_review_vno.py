# Generated by Django 5.0.1 on 2024-03-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_user_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_review',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='user_review',
            name='vno',
            field=models.IntegerField(default='0'),
        ),
    ]
