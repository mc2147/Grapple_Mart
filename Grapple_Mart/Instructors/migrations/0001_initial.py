from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0007_auto_20171007_1122'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=100)),
                ('Description', models.CharField(default='', max_length=1000)),
                ('Topic', models.CharField(default='', max_length=20)),
                ('Confirmed', models.BooleanField(default=False)),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Instructors.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=20)),
                ('Ordered_ID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='E_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Bio', tinymce.models.HTMLField()),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
                ('Owner', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Instructors.Instructor')),
            ],
        ),
        migrations.AddField(
            model_name='e_book',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Instructors.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Instructors.Instructor'),
        ),
    ]
