# Generated by Django 4.2.7 on 2025-01-20 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nourish_home', '0006_remove_recipe_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
    ]
