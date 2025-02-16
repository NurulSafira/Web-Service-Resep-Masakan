# Generated by Django 5.0.6 on 2024-05-14 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm_app', '0006_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuUtama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_last_update', models.DateTimeField(auto_now=True)),
                ('resep_masakans', models.ManyToManyField(related_name='menu_utama', to='rm_app.detailresepmasakan')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_create_menu_utama', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_update_menu_utama', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
