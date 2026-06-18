# Ассинхронность
# 1)async def - корутина. Возвращает
# план действия
# 2) await - ожидание. Ждет внешнее
# событие. временно отодает управление
# для выполнения других задач.

# import time
#
# def run_washing_machine():
#     print('[стирка]Включена')
#     time.sleep(3)
#     print('[стирка]Окончена')
#
# def bake_chicken():
#     print('[духовка]Включена')
#     time.sleep(5)
#     print('[духовка]Окончена')
#
# def main():
#     start = time.time()
#     run_washing_machine()
#     bake_chicken()
#     end = time.time()
#     print(end-start)
# main() #8.000576257705688
#
# import asyncio
#
# async  def run_washing_machine_a():
#     print('[стирка]Включена')
#     await asyncio.sleep(3)
#     print('[стирка]Окончена')
#     return 'чистая одежда'
#
# async def bake_chicken_a():
#     print('[духовка]Включена')
#     await asyncio.sleep(5)
#     print('[духовка]Окончена')
#     return 'вкусный ужин'
#
# async def main_a():
#     start = time.time()
#     result = await asyncio.gather(run_washing_machine_a(), bake_chicken_a())
#     end = time.time()
#     print(result)
#     print(end-start)
#
# asyncio.run(main_a())


# print(time.time()) #1781006102.763668

# .gather()   .create_task()
# 1)Когда жесткое планирование.
# важен финальный результат всех
# задач сразу
# 2)фоновый процесс
# cancel() отмена выполнения задачи
# done() проверить закончено ли выполнение

import asyncio
import time
async def robot_cleaner():
    print('[пылесос]начал уборку')
    for i in range(1, 5):
        await asyncio.sleep(1)
        print(f'[пылесос] {i}')
    print('[пылесос]уборка завершена')
    return 'чистая квартира'
async def main():
    start = time.time()
    vacuum_task = asyncio.create_task(robot_cleaner())
    print('[я]пошел смотреть сериал')
    await asyncio.sleep(2)
    print('[я]проверю пылесос')
    if vacuum_task.done():
        print('[я]пылесос убрался')
    else:
        print('[я]еще работает')
        vacuum_task.cancel()
        try:
            result = await vacuum_task
            print(f'[я]отчет:{result}')
        except asyncio.CancelledError:
            print('уборка прервана')
    end = time.time()
    print(end-start)

asyncio.run(main())

# Event loop - событийный цикл
# бесконечный цикл который мониторит
# состояние задач, переключает
# контекст и распределяет процессорное
# время
# yield from
# итераторы и генераторы
'''Алгоритм выполнения 
1. Регистрация: asyncio.run(main())
2. Polling(опрос): цикл проверяет 
список готовых к выполнению задач.
Если задача активна, выполняется пока
не встретит await
3.Прерывание: корутина приостанавливает
свое выполнение, сохраняя текущее
состояние и передает управление в цикл
4.Ожидание: цикл передает системный
запрос ОС. Пока ОС ждет данные,
Event loop выполняет следующую готовую
задачу
'''
# import asyncio
# import time


# FIFO
# LIFO








