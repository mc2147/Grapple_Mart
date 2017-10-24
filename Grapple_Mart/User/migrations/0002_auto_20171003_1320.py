from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
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
            name='E_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=20)),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyer', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Video_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buyers', models.ManyToManyField(default='', to='User.Athlete')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='Followers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
        migrations.AddField(
            model_name='video_product',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='Seller',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='product',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AddField(
            model_name='e_book',
            name='Owner',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
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
            model_name='athlete',
            name='Products',
            field=models.ManyToManyField(default='', to='User.Product'),
        ),
    ]
