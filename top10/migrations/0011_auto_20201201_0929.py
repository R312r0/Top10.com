# Generated by Django 3.1.3 on 2020-12-01 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0010_auto_20201201_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_text',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='top10.post'),
        ),
    ]
