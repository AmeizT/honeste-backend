# Generated by Django 4.2.1 on 2023-06-11 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0006_remove_demographics_church_remove_member_church_and_more'),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('other_names', models.CharField(blank=True, max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('title', models.CharField(choices=[('Mr', 'Mr.'), ('Ms', 'Ms.'), ('Mrs', 'Mrs.'), ('Dr', 'Dr.'), ('Prof', 'Prof.')], max_length=255)),
                ('dob', models.DateField()),
                ('date_of_baptism', models.DateField(blank=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Known', 'Not Known')], max_length=255)),
                ('relationship', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('None', 'None')], max_length=255)),
                ('address', models.TextField(blank=True)),
                ('country', models.CharField(max_length=255)),
                ('work', models.CharField(blank=True, max_length=255)),
                ('contacts', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('membersince', models.DateField()),
                ('ministry', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='church.church')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
                'ordering': ['surname'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sunday', models.BigIntegerField(default=0)),
                ('home', models.BigIntegerField(default=0)),
                ('friday', models.BigIntegerField(default=0)),
                ('outreach', models.BigIntegerField(default=0)),
                ('kids', models.BigIntegerField(default=0)),
                ('adults', models.BigIntegerField(default=0)),
                ('visitors', models.BigIntegerField(default=0)),
                ('new', models.BigIntegerField(default=0)),
                ('baptized', models.BigIntegerField(default=0)),
                ('repented', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='timetable.timetable')),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register', to='timetable.timetable')),
            ],
            options={
                'verbose_name': 'attendance',
                'verbose_name_plural': 'attendance',
                'ordering': ['-created_at'],
            },
        ),
    ]
