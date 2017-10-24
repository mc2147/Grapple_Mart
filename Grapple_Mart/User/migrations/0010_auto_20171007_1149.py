from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20171007_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_book',
            name='Owner',
            field=models.ForeignKey(default='E_Books', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
        migrations.AlterField(
            model_name='video_product',
            name='Owner',
            field=models.ForeignKey(default='Video_Products', on_delete=django.db.models.deletion.CASCADE, to='User.Instructor'),
        ),
    ]
