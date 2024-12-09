# Generated by Django 5.1 on 2024-10-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=9000)),
                ('product_desc', models.CharField(max_length=9000)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]