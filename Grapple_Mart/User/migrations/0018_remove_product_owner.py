from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0017_course_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Owner',
        ),
    ]
