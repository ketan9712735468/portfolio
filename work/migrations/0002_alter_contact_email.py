# Generated by Django 3.2.4 on 2021-10-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]
