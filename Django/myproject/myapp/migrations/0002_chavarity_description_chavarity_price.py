# Generated by Django 5.1.2 on 2024-10-14 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chavarity',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chavarity',
            name='price',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=5),
        ),
    ]
