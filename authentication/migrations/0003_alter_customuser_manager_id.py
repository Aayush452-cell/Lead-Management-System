# Generated by Django 4.0.2 on 2022-02-24 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_manager_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='manager_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
