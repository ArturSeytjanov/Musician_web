# Generated by Django 4.2.2 on 2023-07-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_product_options_alter_repair_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('G', 'Bad'), ('B', 'Good')], max_length=2, null=True),
        ),
    ]
