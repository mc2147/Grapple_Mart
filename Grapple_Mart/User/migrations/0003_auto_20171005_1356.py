from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20171003_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='instructor',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
