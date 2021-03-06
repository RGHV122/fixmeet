# Generated by Django 2.2.13 on 2020-06-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Appointments')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='FreeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('appointed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='appointments',
            name='details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FreeTime'),
        ),
    ]
