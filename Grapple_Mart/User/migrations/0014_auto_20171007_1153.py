from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_instructor_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Courses', to='User.Instructor'),
        ),
    ]
