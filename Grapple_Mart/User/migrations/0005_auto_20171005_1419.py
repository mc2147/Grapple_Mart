from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20171005_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Buyers',
            field=models.ManyToManyField(default='', null=True, to='User.Athlete'),
        ),
        migrations.AlterField(
            model_name='product',
            name='Owner',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
    ]
