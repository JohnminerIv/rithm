# Generated by Django 2.2.6 on 2020-03-02 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_auto_20200130_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]