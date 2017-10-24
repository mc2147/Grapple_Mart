from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_product_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Owner',
        ),
    ]
