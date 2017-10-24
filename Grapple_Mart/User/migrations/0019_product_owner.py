from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_remove_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Owner',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='User.Instructor'),
        ),
    ]
