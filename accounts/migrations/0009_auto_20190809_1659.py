# Generated by Django 2.2.3 on 2019-08-09 11:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_merge_20190214_1427'),
        ('accounts', '0008_account_assigned_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='sent_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='sender',
            new_name='from_account',
        ),
        migrations.RemoveField(
            model_name='email',
            name='recipient',
        ),
        migrations.AddField(
            model_name='email',
            name='from_email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='recipients',
            field=models.ManyToManyField(related_name='recieved_email', to='contacts.Contact'),
        ),
        migrations.AddField(
            model_name='email',
            name='rendered_message_body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='scheduled_date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='scheduled_later',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='email',
            name='timezone',
            field=models.CharField(default='UTC', max_length=100),
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_email_log', to='contacts.Contact')),
                ('email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_log', to='accounts.Email')),
            ],
        ),
    ]