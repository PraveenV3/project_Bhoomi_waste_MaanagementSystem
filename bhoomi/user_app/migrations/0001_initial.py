# Generated by Django 5.1.7 on 2025-05-19 00:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(blank=True, max_length=15)),
                ('district', models.CharField(blank=True, choices=[('District 1', 'District 1'), ('District 2', 'District 2'), ('District 3', 'District 3'), ('District 4', 'District 4'), ('District 5', 'District 5'), ('District 6', 'District 6'), ('District 7', 'District 7'), ('District 8', 'District 8'), ('District 9', 'District 9'), ('District 10', 'District 10'), ('District 11', 'District 11'), ('District 12', 'District 12'), ('District 13', 'District 13'), ('District 14', 'District 14'), ('District 15', 'District 15'), ('District 16', 'District 16'), ('District 17', 'District 17'), ('District 18', 'District 18'), ('District 19', 'District 19'), ('District 20', 'District 20'), ('District 21', 'District 21'), ('District 22', 'District 22'), ('District 23', 'District 23'), ('District 24', 'District 24')], max_length=50)),
                ('province', models.CharField(blank=True, choices=[('Province 1', 'Province 1'), ('Province 2', 'Province 2'), ('Province 3', 'Province 3'), ('Province 4', 'Province 4'), ('Province 5', 'Province 5'), ('Province 6', 'Province 6'), ('Province 7', 'Province 7'), ('Province 8', 'Province 8'), ('Province 9', 'Province 9')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
