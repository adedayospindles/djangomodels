# Generated by Django 4.0.5 on 2022-06-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(),
        ),
    ]