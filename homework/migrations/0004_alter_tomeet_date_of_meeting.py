# Generated by Django 4.0.1 on 2022-03-17 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_goal_for_month_goal_alter_tomeet_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateTimeField(),
        ),
    ]
