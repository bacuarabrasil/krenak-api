# Generated by Django 3.1.7 on 2021-05-06 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('done', models.BooleanField(blank=True, default=False, null=True, verbose_name='Done')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('text', models.CharField(blank=True, max_length=30, null=True, verbose_name='Text')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_active', models.BooleanField(db_index=True, default=True)),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('comments', models.ManyToManyField(to='activities.Comment', verbose_name='Comments')),
                ('tasks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.task', verbose_name='Tasks')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
