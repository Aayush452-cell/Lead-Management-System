# Generated by Django 4.0.2 on 2022-02-25 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_customuser_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField(default=9999999999, unique=True)),
                ('status', models.CharField(choices=[('hot', 'hot'), ('cold', 'cold'), ('med', 'med'), ('sold', 'sold')], max_length=32)),
                ('sales_representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
