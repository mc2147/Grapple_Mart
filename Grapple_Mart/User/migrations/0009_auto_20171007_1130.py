from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('User', '0008_athlete_following'),
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
            ],
        ),
        migrations.CreateModel(
            name='Course_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=20)),
                ('Ordered_ID', models.IntegerField(default=0)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Items', to='User.Course')),
            ],
        ),
        migrations.CreateModel(
            name='E_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Bio', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Video_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='athlete',
            name='Products',
            field=models.ManyToManyField(default='', to='User.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='Buyers',
            field=models.ManyToManyField(default='', null=True, to='User.Athlete'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='Following',
            field=models.ManyToManyField(default='', to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='video_product',
            name='Buyers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='video_product',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Buyer',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Seller',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='Followers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='e_book',
            name='Buyers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='e_book',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='Buyers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='course',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='Courses',
            field=models.ManyToManyField(to='User.Course'),
        ),
        migrations.AddField(
            model_name='product',
            name='Owner',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
    ]
