# Generated by Django 2.2.2 on 2019-06-23 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['author_name']},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='author_name',
        ),
    ]