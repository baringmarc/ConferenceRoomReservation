# Generated by Django 3.2.6 on 2022-03-01 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomReservation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning', models.IntegerField(blank=True, null=True)),
                ('afternoon', models.IntegerField(blank=True, null=True)),
                ('evening', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning', models.BooleanField(default=False)),
                ('afternoon', models.BooleanField(default=False)),
                ('evening', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='date',
            new_name='dateOfUse',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='conferenceRoom',
            new_name='room',
        ),
        migrations.AddField(
            model_name='applicant',
            name='firstName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='lastName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='conferenceroom',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reservation',
            name='dateReserved',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='conferenceroom',
            name='fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomReservation.fee'),
        ),
    ]
