# Generated by Django 4.1.1 on 2022-10-12 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(blank=True, max_length=200)),
                ('address_line_2', models.CharField(blank=True, max_length=200)),
                ('profile_picture', models.ImageField(blank=True, upload_to='UserProfile')),
                ('city', models.CharField(blank=True, max_length=25)),
                ('state', models.CharField(blank=True, max_length=25)),
                ('country', models.CharField(blank=True, max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
