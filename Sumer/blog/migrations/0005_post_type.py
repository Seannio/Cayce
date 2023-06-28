# Generated by Django 4.2.2 on 2023-06-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'BLOGPOST'), (1, 'ART'), (2, 'MUSIC')], default=0),
        ),
    ]