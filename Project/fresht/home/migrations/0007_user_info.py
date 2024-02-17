# Generated by Django 5.0.1 on 2024-01-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_movies_surprises'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=75, verbose_name='Username')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Id')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]
