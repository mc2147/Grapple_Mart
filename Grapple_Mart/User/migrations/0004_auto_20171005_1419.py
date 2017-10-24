from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20171005_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='File',
            field=models.FileField(default='', upload_to='Products'),
        ),
        migrations.AddField(
            model_name='product',
            name='Thumbnail',
            field=models.FileField(default='', upload_to='Products/Thumbnails'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
