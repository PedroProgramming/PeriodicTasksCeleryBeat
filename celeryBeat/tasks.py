from celery import shared_task
from datetime import datetime
from .models import DataAtual

@shared_task
def my_task():
    return 'teste'


@shared_task(bind=True)
def atualiza_banco(self):
    data_atual = DataAtual.objects.all().first()
    data_atual.data_atual = datetime.now()
    data_atual.save()
    return 'Done'