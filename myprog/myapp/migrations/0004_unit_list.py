# Generated by Django 5.1.3 on 2024-11-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_classification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_measure', models.CharField(max_length=50)),
            ],
        ),
    ]
