# Generated by Django 3.1.3 on 2021-04-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=100)),
                ('person_a', models.CharField(max_length=100)),
                ('a_id', models.CharField(max_length=100)),
                ('person_b', models.CharField(max_length=100)),
                ('b_id', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('book', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]