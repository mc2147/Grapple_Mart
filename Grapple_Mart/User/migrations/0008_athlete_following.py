from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instructors', '0002_auto_20171007_1128'),
        ('User', '0007_auto_20171007_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='Following',
            field=models.ManyToManyField(default='', to='Instructors.Instructor'),
        ),
    ]
