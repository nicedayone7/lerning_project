# Generated by Django 3.0.2 on 2022-04-01 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='arts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.Category'),
        ),
    ]
