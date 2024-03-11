# Generated by Django 5.0.3 on 2024-03-11 10:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='dishtype',
            options={'verbose_name': 'Типы блюд', 'verbose_name_plural': 'Типы блюд'},
        ),
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ингредиент', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='категории блюд (завтрак, обед, ужин)', max_length=500, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='dishtype',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='dishtype',
            name='title',
            field=models.CharField(help_text='типы блюд (первое, второе, напитки, десерт)', max_length=500, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='name',
            field=models.CharField(max_length=500, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='количество'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='unit',
            field=models.CharField(help_text='единица измерения (грамм, литр)', max_length=500, verbose_name='единица'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='категории блюд'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dish_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.dishtype', verbose_name='типы блюд'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ingredients', verbose_name='ингредиенты'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255, verbose_name='название'),
        ),
    ]
