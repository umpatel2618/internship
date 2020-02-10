# Generated by Django 3.0.2 on 2020-02-05 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cleaner',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_score', models.FloatField(default=0.0)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.City')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]