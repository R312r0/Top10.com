# Generated by Django 3.1.4 on 2020-12-08 20:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0021_tablevalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]