# Generated by Django 3.2.14 on 2022-07-13 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0002_rename_brandmodel_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.TextField(max_length=64, unique=True)),
                ('name', models.TextField(max_length=128)),
                ('price', models.DecimalField(decimal_places=5, max_digits=15)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='brands.brand')),
            ],
            options={
                'ordering': ('name', 'sku'),
            },
        ),
    ]