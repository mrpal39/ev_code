# Generated by Django 3.1.3 on 2020-11-14 04:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_feeds_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='feeds',
            name='content',
        ),
        migrations.RemoveField(
            model_name='feeds',
            name='description',
        ),
    ]