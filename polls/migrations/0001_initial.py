# Generated by Django 2.2.6 on 2019-10-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
                ('pw', models.CharField(max_length=10)),
                ('birth', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('subject', models.CharField(max_length=1)),
            ],
        ),
    ]
