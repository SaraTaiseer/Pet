# Generated by Django 3.0.3 on 2020-02-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petApp', '0002_auto_20200217_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
