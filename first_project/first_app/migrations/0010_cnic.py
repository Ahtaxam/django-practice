# Generated by Django 4.1 on 2024-10-04 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_person_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cnic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('expiry_data', models.DateField()),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='first_app.person')),
            ],
        ),
    ]
