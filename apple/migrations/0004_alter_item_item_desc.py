# Generated by Django 5.1 on 2024-11-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0003_item_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(max_length=9000),
        ),
    ]
