# Generated by Django 4.2.3 on 2023-07-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField(max_length=20)),
            ],
        ),
    ]
