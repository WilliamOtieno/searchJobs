# Generated by Django 3.1.3 on 2020-11-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.TextField(max_length=50)),
                ('subfield', models.TextField(max_length=100)),
                ('company_name', models.TextField(max_length=50)),
                ('county', models.TextField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.TextField()),
            ],
        ),
    ]
