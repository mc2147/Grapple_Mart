from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20171005_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Has_Thumbnail',
            field=models.BooleanField(default=False),
        ),
    ]
