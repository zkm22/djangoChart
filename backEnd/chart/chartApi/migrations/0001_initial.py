# Generated by Django 2.2.2 on 2019-06-09 05:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=10)),
                ('nth', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Table2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area1', models.IntegerField()),
                ('area2', models.IntegerField()),
                ('nth', models.IntegerField()),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
