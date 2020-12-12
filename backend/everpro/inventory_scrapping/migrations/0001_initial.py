# Generated by Django 3.0.5 on 2020-12-10 21:28

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('asin', models.CharField(max_length=20, unique=True)),
                ('platform', models.CharField(max_length=20)),
                ('zone', models.CharField(max_length=20)),
                ('stock_info', models.CharField(blank=True, max_length=20)),
                ('all_other_details', models.TextField(blank=True, null=True)),
                ('product_name', models.CharField(blank=True, max_length=20)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]