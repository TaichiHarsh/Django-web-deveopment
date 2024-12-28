# Generated by Django 4.2.3 on 2023-07-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('course_fees', models.IntegerField()),
                ('course_duration', models.CharField(max_length=40)),
                ('course_contents', models.TextField(blank=True)),
            ],
        ),
    ]
