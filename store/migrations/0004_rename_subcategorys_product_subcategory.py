# Generated by Django 4.1.1 on 2022-09-22 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='subcategorys',
            new_name='subcategory',
        ),
    ]