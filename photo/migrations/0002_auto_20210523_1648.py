# Generated by Django 3.2.3 on 2021-05-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo.tags'),
        ),
    ]
