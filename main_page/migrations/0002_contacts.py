# Generated by Django 3.0.4 on 2020-05-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('intagram_url', models.URLField(blank=True, null=True)),
                ('vk_url', models.URLField(blank=True, null=True)),
                ('fb_url', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
