# Generated by Django 3.0.2 on 2020-01-09 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='产品名称')),
                ('isenabled', models.BooleanField(blank=True, default=True, verbose_name='产品状态')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='产品描述')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='UserAndProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Product')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='项目名称')),
                ('version', models.CharField(blank=True, max_length=32, null=True, verbose_name='版本')),
                ('isenabled', models.BooleanField(default=True, verbose_name='状态')),
                ('descr', models.TextField(blank=True, null=True, verbose_name='项目描述')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Product', verbose_name='产品名称')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='模块名称')),
                ('isenabled', models.BooleanField(default=True, verbose_name='状态')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('createat', models.CharField(blank=True, max_length=32, null=True, verbose_name='创建者')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('updateat', models.CharField(blank=True, max_length=32, null=True, verbose_name='更新者')),
                ('sortby', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.Project', verbose_name='所属项目')),
            ],
            options={
                'ordering': ['-sortby'],
            },
        ),
    ]
