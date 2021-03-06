# Generated by Django 4.0 on 2021-12-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('face', '0010_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('photo', models.ImageField(blank=True, upload_to='clients_photos')),
                ('fr', models.CharField(max_length=100000)),
            ],
        ),
    ]
