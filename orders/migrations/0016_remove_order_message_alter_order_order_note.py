# Generated by Django 4.1.1 on 2022-10-10 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_rename_order_total_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='message',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]