from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_course_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
