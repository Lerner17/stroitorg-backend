# Generated by Django 3.0.4 on 2020-07-22 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_category_is_thin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thickness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Thickness'),
        ),
    ]
