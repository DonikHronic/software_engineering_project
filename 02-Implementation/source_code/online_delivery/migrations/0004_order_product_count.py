# Generated by Django 5.1.3 on 2024-12-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_delivery", "0003_alter_order_options_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="product_count",
            field=models.IntegerField(default=1),
        ),
    ]