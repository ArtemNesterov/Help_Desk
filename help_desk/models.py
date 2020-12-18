from django.db import models

from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL
"""
time to create and update applications
"""


class TimeStampModel(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


"""
request and its characteristics
"""


class ClaimModel(TimeStampModel):
    DRAFT = 'DR'
    PENDING = 'PN'
    IN_PROGRESS = 'IP'
    DONE = 'DN'
    DECLINED = 'DC'

    LOW = 'LW'
    MEDIUM = 'MD'
    HIGH = 'HG'

    INSTALLATION = 'INS'
    SETTINGS = 'SET'
    REPAIRS = 'REP'

    STATUSES = (
        (DRAFT, 'Draft'),
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In progress'),
        (DONE, 'Done'),
        (DECLINED, 'Declined'),
    )

    PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    TOPICS = (
        (INSTALLATION, 'Installation'),
        (SETTINGS, 'Settings'),
        (REPAIRS, 'Repairs'),
    )

    claim_topic = models.CharField(choices=TOPICS, max_length=30)
    text = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    status = models.CharField(choices=STATUSES, max_length=2, default=DRAFT)
    priority = models.CharField(choices=PRIORITY, max_length=2, default=LOW)
    author = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    declined_status_count = models.PositiveSmallIntegerField(default=0)


"""
comments to requests
"""


class CommentModel(TimeStampModel):
    claim = models.ForeignKey(ClaimModel, on_delete=models.SET_NULL, blank=True, null=True)
    author = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.TextField()
    declined_status_count = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('create_at',)
