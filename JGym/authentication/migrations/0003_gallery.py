# Generated by Django 4.2.5 on 2023-10-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_enrollment_membershipplan_trainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
    ]
