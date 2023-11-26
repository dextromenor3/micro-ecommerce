# Generated by Django 4.1.13 on 2023-11-22 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('handle', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, default=9.99, max_digits=10)),
                ('og_price', models.DecimalField(decimal_places=2, default=9.99, max_digits=10)),
                ('stripe_price', models.IntegerField(default=999)),
                ('price_changed_timestamp', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
