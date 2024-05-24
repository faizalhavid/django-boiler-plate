# Generated by Django 4.2.10 on 2024-05-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_proposal_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assesmentsubmissionsproposal',
            name='status',
        ),
        migrations.RemoveField(
            model_name='submissionsproposalapply',
            name='tags',
        ),
        migrations.AlterField(
            model_name='submissionsproposalapply',
            name='status',
            field=models.CharField(choices=[('APPLIED', 'Applied'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('REVISION', 'Revision'), ('PASSED', 'Passed'), ('PASSED FUNDING', 'Passed Funding')], default='APPLIED', max_length=15),
        ),
    ]