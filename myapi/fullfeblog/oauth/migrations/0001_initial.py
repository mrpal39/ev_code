# Generated by Django 3.0 on 2021-03-02 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('weibo', 'weibo'), ('google', 'google'), ('github', 'GitHub'), ('facebook', 'FaceBook'), ('qq', 'QQ')], default='a', max_length=10, verbose_name='类型')),
                ('appkey', models.CharField(max_length=200, verbose_name='AppKey')),
                ('appsecret', models.CharField(max_length=200, verbose_name='AppSecret')),
                ('callback_url', models.CharField(default='http://www.baidu.com', max_length=200, verbose_name='回调地址')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': 'oauthconfigrations',
                'verbose_name_plural': 'oauthconfigrations',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50)),
                ('nikename', models.CharField(max_length=50, verbose_name='nickname')),
                ('token', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.CharField(blank=True, max_length=350, null=True)),
                ('type', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('matedata', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_time')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='modification time')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'oauthuser',
                'verbose_name_plural': 'oauthuser',
                'ordering': ['-created_time'],
            },
        ),
    ]
