# Generated by Django 2.2.28 on 2022-12-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='name of the medicine', max_length=200)),
                ('name_of_manufacturer', models.CharField(help_text='name of the manufacturer', max_length=200, null=True)),
                ('price', models.IntegerField(help_text='Enter the MRP value of the medicine', max_length=1000, verbose_name='M.R.P')),
                ('description', models.TextField(help_text='Enter a short description on the product', max_length=2000)),
                ('date_of_manufacture', models.DateField(blank=True, help_text='Date of the product manufacture', null=True)),
            ],
        ),
    ]
