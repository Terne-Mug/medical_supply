# Generated by Django 2.2 on 2020-04-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200409_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='additional',
            field=models.TextField(),
        ),
    ]
