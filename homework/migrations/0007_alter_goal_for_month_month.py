# Generated by Django 4.0.1 on 2022-03-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0006_alter_tomeet_date_of_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_for_month',
            name='month',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
