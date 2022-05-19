# Generated by Django 4.0.4 on 2022-05-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='id_back',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='id_front',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.CharField(max_length=400),
        ),
    ]