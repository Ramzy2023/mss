# Generated by Django 5.1.3 on 2024-11-08 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='office_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
