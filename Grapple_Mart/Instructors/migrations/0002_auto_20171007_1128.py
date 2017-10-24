from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='e_book',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='video_product',
            name='Buyers',
        ),
    ]
