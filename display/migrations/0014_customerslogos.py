# Generated by Django 3.0.4 on 2020-03-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0013_auto_20200326_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomersLogos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
