# Generated by Django 3.1.3 on 2020-12-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0007_auto_20201130_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='postitem',
            name='item_picture',
            field=models.ImageField(default='No image aviable!', upload_to='gallery'),
        ),
        migrations.AddField(
            model_name='postitem',
            name='place_in_top',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='1'),
        ),
    ]
