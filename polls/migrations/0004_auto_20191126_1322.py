# Generated by Django 2.2.7 on 2019-11-26 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20191126_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
