# Generated by Django 4.2.7 on 2025-01-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nourish_home', '0005_recipe_categories_alter_recipecategory_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AlterField(
            model_name='recipecategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nourish_home.category'),
        ),
    ]
