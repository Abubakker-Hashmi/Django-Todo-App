# Generated by Django 4.2.2 on 2023-07-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="datecompleted",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
