# Generated by Django 4.2.3 on 2023-07-26 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='feedAuthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL),
        ),
    ]