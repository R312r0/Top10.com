# Generated by Django 3.1.4 on 2020-12-08 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0018_post_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postitem',
            name='table_row',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='top10.table'),
        ),
    ]
