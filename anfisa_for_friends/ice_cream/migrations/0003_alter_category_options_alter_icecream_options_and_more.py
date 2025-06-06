# Generated by Django 5.2.1 on 2025-06-04 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_alter_category_options_alter_icecream_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'мороженое', 'verbose_name_plural': 'мороженое'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'топпинг', 'verbose_name_plural': 'топпинги'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'обёртку', 'verbose_name_plural': 'обёртки'},
        ),
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Порядок отображения'),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='icecream',
            name='toppings',
            field=models.ManyToManyField(to='ice_cream.topping', verbose_name='Топпинги'),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='wrapper',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ice_cream', to='ice_cream.wrapper', verbose_name='Обёртка'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]
