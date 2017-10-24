from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20171007_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_book',
            name='Owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='E_Books', to='User.Instructor'),
        ),
        migrations.AlterField(
            model_name='video_product',
            name='Owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Video_Products', to='User.Instructor'),
        ),
    ]
