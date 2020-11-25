# Generated by Django 3.0.3 on 2020-02-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temp', models.FloatField()),
                ('voltage', models.FloatField()),
                ('current', models.FloatField()),
                ('speed', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('status', models.CharField(max_length=1000)),
            ],
        ),
    ]