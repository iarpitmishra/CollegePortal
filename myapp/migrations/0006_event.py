# Generated by Django 4.2.3 on 2023-08-03 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_employee_employee_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_venue', models.CharField(max_length=100)),
                ('event_pic', models.FileField(default='', upload_to='myapp/event_pic')),
                ('event_description', models.TextField()),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
