# Generated by Django 5.0 on 2023-12-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_profile_user_profile_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='cart', to='main_app.item'),
        ),
    ]
