# Generated by Django 2.1b1 on 2018-07-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=500)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=50)),
                ('averageGrade', models.CharField(max_length=20)),
                ('graduateYear', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('companyName', models.CharField(max_length=40)),
                ('aboutJob', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=50)),
                ('usedLanguage', models.CharField(max_length=20)),
                ('aboutProject', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillField', models.CharField(max_length=40)),
                ('skilledIn', models.CharField(max_length=100)),
            ],
        ),
    ]
