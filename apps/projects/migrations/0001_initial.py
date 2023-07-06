# Generated by Django 4.2.1 on 2023-07-05 14:00

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('church', '0007_church_pastor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('cost', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('location', models.CharField(max_length=255)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('church', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='church.church')),
                ('managers', models.ManyToManyField(blank=True, related_name='project_managers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ['-created'],
            },
        ),
    ]