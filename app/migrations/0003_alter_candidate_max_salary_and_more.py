# Generated by Django 4.0.5 on 2022-07-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_candidate_max_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='max_salary',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='min_salary',
            field=models.BigIntegerField(default=0),
        ),
    ]