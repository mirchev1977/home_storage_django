# Generated by Django 3.1.4 on 2020-12-11 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201211_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000, null=True)),
                ('img_url', models.CharField(max_length=1000, null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.container')),
            ],
        ),
    ]
