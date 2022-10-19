# Generated by Django 4.1.1 on 2022-10-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('pin1', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.CharField(max_length=122)),
                ('pin1', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='ChangePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_password', models.CharField(max_length=122)),
                ('new_password1', models.CharField(max_length=122)),
                ('newpassword2', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='ChangePin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('old_pin', models.CharField(max_length=122)),
                ('new_pin1', models.CharField(max_length=122)),
                ('new_pin2', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('msg', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('date', models.CharField(default='', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Lock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('pin1', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Lock2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('pin1', models.CharField(max_length=122)),
                ('pin2', models.CharField(max_length=122)),
                ('account_number', models.CharField(default='', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=122)),
                ('bank_name', models.CharField(max_length=122)),
                ('mobile_number', models.CharField(max_length=122)),
                ('account_number', models.CharField(max_length=122)),
                ('card_number', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('gender', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('balance', models.FloatField(default=0.0)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MobileRecharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('date', models.CharField(default='', max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=122)),
                ('mobile_number', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='SendMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=122)),
                ('my_account_number', models.CharField(max_length=122)),
                ('account_number', models.CharField(max_length=122)),
                ('confirm_number', models.CharField(max_length=122)),
                ('amount', models.CharField(max_length=122)),
                ('Bank', models.CharField(max_length=122)),
                ('name', models.CharField(default=0, max_length=122)),
                ('email', models.CharField(default='', max_length=122)),
                ('date', models.CharField(default='', max_length=122)),
                ('holder_name', models.CharField(default=0, max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('Loginpassword', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount2', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('date', models.CharField(default='', max_length=122)),
            ],
        ),
    ]
