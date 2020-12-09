# Generated by Django 3.1.4 on 2020-12-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0023_auto_20201208_2323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='importance',
        ),
        migrations.AddField(
            model_name='post',
            name='importance',
            field=models.CharField(choices=[('Must read', 'Must read'), ('Hot this week', 'Hot this week')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='PostImportance',
        ),
    ]
