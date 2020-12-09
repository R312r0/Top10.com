# Generated by Django 3.1.3 on 2020-11-30 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top10', '0004_auto_20201130_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefit_title', models.CharField(max_length=200, verbose_name='Benefit title')),
                ('benefit_desc', models.CharField(max_length=200, verbose_name='Benefit description')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='top10.postitem')),
            ],
        ),
    ]
