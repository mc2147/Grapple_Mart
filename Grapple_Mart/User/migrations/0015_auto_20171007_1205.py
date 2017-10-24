from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_auto_20171007_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_item',
            name='Description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='course_item',
            name='File',
            field=models.FileField(default='', upload_to='Course_Items'),
        ),
    ]
