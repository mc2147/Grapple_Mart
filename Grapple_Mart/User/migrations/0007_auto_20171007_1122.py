from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_product_has_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Owner',
        ),
        migrations.RemoveField(
            model_name='course_files',
            name='Course',
        ),
        migrations.RemoveField(
            model_name='e_book',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='e_book',
            name='Owner',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='Followers',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='User',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Buyer',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Seller',
        ),
        migrations.RemoveField(
            model_name='video_product',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='video_product',
            name='Owner',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='Courses',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='Following',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='Products',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Buyers',
        ),
        migrations.RemoveField(
            model_name='product',
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
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Video_Product',
        ),
    ]
