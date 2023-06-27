# Generated by Django 3.2.5 on 2023-02-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=150)),
                ('icon', models.CharField(default='', max_length=200)),
            ],
        ),
    ]