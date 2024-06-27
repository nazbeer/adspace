# Generated by Django 5.0.6 on 2024-06-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='vendor',
        ),
        migrations.AddField(
            model_name='catalog',
            name='vender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='vender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
