# Generated by Django 2.1.4 on 2019-01-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20190107_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
