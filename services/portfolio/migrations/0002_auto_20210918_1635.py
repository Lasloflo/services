# Generated by Django 3.2.7 on 2021-09-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название категории услуг'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='large_image',
            field=models.ImageField(help_text='1200х801', upload_to='static/images/portfolio', verbose_name='Большая картинка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='small_description',
            field=models.CharField(help_text='max 32 символ', max_length=32, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='small_image',
            field=models.ImageField(help_text='470х330', upload_to='static/images/portfolio', verbose_name='Маленькая картинка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(help_text='max 21 символа', max_length=21, verbose_name='Название услуги'),
        ),
    ]