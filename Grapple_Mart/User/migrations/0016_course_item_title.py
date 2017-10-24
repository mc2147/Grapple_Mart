from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_auto_20171007_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_item',
            name='Title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
