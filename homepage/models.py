from django.db import models

STATUS_APP = (
    ('OnGoing' ,'On-Going'),
    ('Finish', 'Finish'),
)

class Home(models.Model):
    class Meta:
        verbose_name_plural = 'home'

    url = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    date_start = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status_app = models.SmallIntegerField(choices=STATUS_APP)

    def __str__(self):
        return self.title
