# Generated by Django 3.1.5 on 2021-04-08 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210211_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Catégorie', 'verbose_name_plural': 'Catégories'},
        ),
        migrations.AlterModelOptions(
            name='subcateory',
            options={'ordering': ('name',), 'verbose_name': 'Sous Catégorie', 'verbose_name_plural': 'sous Catégories'},
        ),
        migrations.AddField(
            model_name='product',
            name='show_home',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='color',
            name='hex_value',
            field=models.CharField(max_length=7, verbose_name='Valeur hexadécimale'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Nom couleur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Nom produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('N', 'Nouveau'), ('R', 'Rupture'), ('P', 'Promotion'), ('S', 'SANS')], default='N', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subcateory', verbose_name='Sous catégorie'),
        ),
        migrations.AlterField(
            model_name='subcateory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='main.category', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='subcateory',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Sous Catégorie'),
        ),
        migrations.AlterField(
            model_name='subcateory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Sous Catégorie'),
        ),
        migrations.AlterField(
            model_name='taille',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Nom taille'),
        ),
    ]
