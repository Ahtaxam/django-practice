# Generated by Django 4.1 on 2024-10-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_alter_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
    ]
