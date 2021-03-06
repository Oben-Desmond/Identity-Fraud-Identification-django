# Generated by Django 4.0.4 on 2022-05-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200)),
                ('lng', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
    ]
