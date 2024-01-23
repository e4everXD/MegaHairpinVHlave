# Generated by Django 4.2.7 on 2024-01-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairpin', '0015_alter_post_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=15, null=True),
        ),
    ]
