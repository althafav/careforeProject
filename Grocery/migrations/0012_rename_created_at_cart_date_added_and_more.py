# Generated by Django 4.1.1 on 2022-09-28 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0013_alter_productattribute_color_and_more'),
        ('Grocery', '0011_rename_date_added_cart_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='created_at',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('Cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Grocery.cart')),
                ('Product_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productattribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]