# Generated by Django 3.0.2 on 2020-02-05 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200205_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleaner',
            name='id',
        ),
        migrations.AlterField(
            model_name='cleaner',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]