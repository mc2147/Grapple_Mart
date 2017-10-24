from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20171007_1130'),
        ('Instructors', '0002_auto_20171007_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Owner',
        ),
        migrations.RemoveField(
            model_name='course_files',
            name='Course',
        ),
        migrations.DeleteModel(
            name='Course_Item',
        ),
        migrations.RemoveField(
            model_name='e_book',
            name='Owner',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='User',
        ),
        migrations.RemoveField(
            model_name='video_product',
            name='Owner',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Course_Files',
        ),
        migrations.DeleteModel(
            name='E_Book',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Video_Product',
        ),
    ]
