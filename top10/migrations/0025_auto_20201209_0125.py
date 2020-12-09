# Generated by Django 3.1.4 on 2020-12-08 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0024_auto_20201208_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_title',
            field=models.CharField(max_length=100, null=True, verbose_name='Category title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='importance',
            field=models.CharField(choices=[('Must read', 'Must read'), ('Hot this week', 'Hot this week'), ('Trending', 'Trending')], max_length=200, null=True),
        ),
    ]