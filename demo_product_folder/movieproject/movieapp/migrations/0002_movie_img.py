# Generated by Django 4.1 on 2024-02-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='ghh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
