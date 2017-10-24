from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20171007_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='Followers',
        ),
    ]
