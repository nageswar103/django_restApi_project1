# Generated by Django 3.2.7 on 2021-09-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_auto_20210919_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
