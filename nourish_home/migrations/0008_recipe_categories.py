# Generated by Django 4.2.7 on 2025-01-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nourish_home', '0007_remove_recipe_ingredients_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='nourish_home.category'),
        ),
    ]
