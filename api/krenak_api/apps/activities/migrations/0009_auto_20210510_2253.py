# Generated by Django 3.1.7 on 2021-05-10 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20210506_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='activities.activity', verbose_name='Activity'),
        ),
    ]
