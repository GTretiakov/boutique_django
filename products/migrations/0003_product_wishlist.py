# Generated by Django 3.1.7 on 2021-04-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0002_auto_20210331_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlist', to='profiles.UserProfile'),
        ),
    ]
