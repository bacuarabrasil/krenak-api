# Generated by Django 3.1.7 on 2021-03-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="birthdate",
            field=models.DateField(blank=True, null=True, verbose_name="birth date"),
        ),
    ]