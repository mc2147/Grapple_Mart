from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0012_remove_instructor_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='Followers',
            field=models.ManyToManyField(default='', to='User.Athlete'),
        ),
    ]
