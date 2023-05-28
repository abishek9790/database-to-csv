# Generated by Django 4.1.4 on 2023-05-28 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('year', models.IntegerField(max_length=4)),
                ('men', models.IntegerField()),
                ('women', models.IntegerField()),
                ('men_child', models.IntegerField()),
                ('women_child', models.IntegerField()),
            ],
        ),
    ]