import threading
import time
import asyncio
import random

bank_balance = 1000
balance_lock = threading.Lock()
main_loop = None #ссылка на основной Event Loop
log_queue = None #очередь (FIFO)

def withdraw_cash(amount, atm_name):
    global bank_balance
    with balance_lock:
        print(f'{atm_name}запрос на списание {amount}руб')
        time.sleep(0.1)
        if bank_balance >= amount:
            bank_balance -= amount
            status_msg = f'[СПИСАНИЕ]{bank_balance}-новый баланс'
            print(status_msg)
        else:
            status_msg = f'[ОТКАЗ]{bank_balance} баланс'
            print(status_msg)
    # вызов передачи логов
    # put_nowait-метод очереди(вкладывает)
    main_loop.call_soon_threadsafe(log_queue.put_nowait,
                                   status_msg)


async def async_logger():
    print('(Логгер) Запущен')
    # извлекаем сообщения из очереди
    while True:
        log_entry = await log_queue.get()
        await asyncio.sleep(0.2)
        print(f'Лог получен->{log_entry}')
        #сигнализируем что задача из очереди обработана
        log_queue.task_done()

async def main():
    global log_queue, main_loop
    # get_running_loop-возвращает запущенный цикл событий
    main_loop = asyncio.get_running_loop()
    log_queue = asyncio.Queue() # ассинхронная очередь
    log_task = asyncio.create_task(async_logger())

    # независимые потоки банкоматов
    threads = []
    for i in range(1, 6):
        atm_name = f'Банкомат {1}'
        amount = random.randint(100, 300)
        t = threading.Thread(target=withdraw_cash,
                             args=(amount, atm_name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    await log_queue.join()

    log_task.cancel() #логгер отменяем тк работа завершена

asyncio.run(main())