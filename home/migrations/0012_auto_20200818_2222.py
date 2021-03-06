# Generated by Django 3.0.7 on 2020-08-18 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0011_auto_20200818_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding',
            name='buyer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidding_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trading',
            name='buyer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trading_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trading',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trading_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
