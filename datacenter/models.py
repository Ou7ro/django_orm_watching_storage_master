from django.db import models
import datetime
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    entered_time = localtime(visit.entered_at)
    logged_time = localtime(visit.leaved_at)
    delta = logged_time - entered_time
    return delta


def format_duration(delta):
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    return f'{int(hours):02}:{int(minutes):02}'


def is_visit_long(visit):
    delta = get_duration(visit)
    minutes = datetime.timedelta(hours=1)
    if delta > minutes:
        return True
    else:
        return False
