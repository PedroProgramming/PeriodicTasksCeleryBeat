import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone = settings.CELERY_TIMEZONE)

app.config_from_object('django.conf.settings', namespace='CELERY')

# Celery beat config

app.conf.beat_schedule = {
    'atualiza-banco-todos-dias-00:00': {
        'task': 'celeryBeat.tasks.atualiza_banco',
        # crontab: Responsável pelo agendamento
        'schedule': crontab()
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    pass