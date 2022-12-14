# Generated by Django 4.1.1 on 2022-09-22 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Object unique ID.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=12)),
            ],
            options={
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Object unique ID.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(help_text='The name of the product.', max_length=100)),
                ('description', models.TextField(help_text='The description of the product.', max_length=500)),
                ('price', models.FloatField(default=0.0, help_text='The price of the product.')),
                ('quantity', models.IntegerField(default=0, help_text='How many of this product exists?')),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'products',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, help_text='Object unique ID.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('has_paid', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed')], default='pending', max_length=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'payments',
                'db_table': 'payments',
                'ordering': ['-date_created'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='products.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['user', 'order', 'has_paid', 'date_created'], name='payments_user_id_9d40f4_idx'),
        ),
    ]
