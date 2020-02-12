# Generated by Django 3.0.2 on 2020-02-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ourstory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ourstory', models.CharField(max_length=200)),
                ('ourstorydescription', models.TextField(blank=True)),
                ('storythumbphoto', models.ImageField(blank=True, upload_to='photos/aboutus')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectpartners', models.CharField(max_length=200)),
                ('projectpartnerphoto', models.ImageField(blank=True, upload_to='photos/aboutus')),
                ('projectpartnername', models.CharField(max_length=200)),
                ('projectpartnerdesc', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tourplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('successfultour', models.IntegerField()),
                ('yeartourarrange', models.IntegerField()),
                ('happyclient', models.IntegerField()),
            ],
        ),
    ]