# Generated by Django 3.0.6 on 2020-05-06 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(default='created', max_length=120)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=40.0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='carts.Cart')),
            ],
        ),
    ]
