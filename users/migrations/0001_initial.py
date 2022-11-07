# Generated by Django 4.1.2 on 2022-11-07 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedPost',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(editable=False, max_length=50)),
                ('liked', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['liked'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='UserPosts/')),
                ('caption', models.TextField(blank=True)),
                ('total_likes', models.PositiveIntegerField(default=0, editable=False)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ['user'],
            },
        ),
    ]