from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from django.core import management
from multiprocessing.shared_memory import SharedMemory


def periodic_execution():# 任意の関数名
    # ここに定期実行したい処理を記述する
    management.call_command('batch')


def start():
    try:
        # 共有メモリが取得できた場合は過去に既にapschedulerが実行されているので何もせず処理を抜けます。
        sm = SharedMemory(create=False, name="apscheduler_start")
        return
    except:
        # 共有メモリが取得できなかった場合は初回のapscheduler実行なので共有メモリを登録して処理を続行します。
        shm = SharedMemory(create=True, size=1, name="apscheduler_start")
    # スケジュールで実行する関数を登録
        scheduler = BackgroundScheduler()
        scheduler.add_job(periodic_execution, 'interval', seconds=1)
        scheduler.start()