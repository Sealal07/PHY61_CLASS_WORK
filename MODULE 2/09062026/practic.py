# # Задача 1
# # import asyncio
# # import time
# #
# # async def water_flower(name, duration):
# #     print(f"[Полив] Начинаю поливать {name}...")
# #     await asyncio.sleep(duration)
# #     print(f"[Полив] {name} успешно полит!")
# #     return f"{name} готов"
# #
# # async def main_task_1():
# #     print("Задача 1")
# #     start_time = time.time()
# #     results = await asyncio.gather(
# #         water_flower("Фикус", 2), water_flower("Кактус", 1), water_flower("Орхидея", 3)
# #     )
# #     end_time = time.time()
# #     total_time = end_time - start_time
# #     print("результаты:", results)
# #     print(f"время выполнения: {total_time:.2f} сек. (ожидалось около 3 секунд)")
# #
# # # Задача 2
# # async def download_update():
# #     for i in range(1, 5):
# #         await asyncio.sleep(1)
# #         print(f"[Загрузка] Скачано {i * 25}%...")
# #     return "Обновление установлено"
# #
# #
# # async def main_task_2():
# #     print("Задача 2")
# #     download_task = asyncio.create_task(download_update())
# #     await asyncio.sleep(2)
# #     print("[Я] Разложил вещи на столе...")
# #     print(f"[Статус] Загрузка завершилась? {download_task.done()}")
# #     final_result = await download_task
# #     print(f"[Итог]: {final_result}")
# #
# #
# #
# # async def main():
# #         await main_task_1()
# #         await main_task_2()
# #
# # asyncio.run(main())
#
#
# import asyncio
# import time
#
# async def water_flower(name, duration):
#     print(f"[Полив] Начинаю поливать {name}...")
#     await asyncio.sleep(duration)
#     print(f"[Полив] {name} успешно полит!")
#     return f"{name} готов"
#
# async def download_update():
#     for i in range(1, 5):
#         await asyncio.sleep(1)
#         print(f"[Загрузка] Скачано {i * 25}%...")
#     return "Обновление установлено"
#
# async def main_task_1():
#     print("Задача 1")
#     start_time = time.time()
#     results = await asyncio.gather(
#         water_flower("Фикус", 2),
#         water_flower("Кактус", 1),
#         water_flower("Орхидея", 3)
#     )
#     end_time = time.time()
#     total_time = end_time - start_time
#     print("результаты:", results)
#     print(f"время выполнения: {total_time:.2f} сек. (ожидалось около 3 секунд)")
#     return results
#
# async def main_task_2():
#     print("Задача 2")
#     download_task = asyncio.create_task(download_update())
#     await asyncio.sleep(2)
#     print("[Я] Разложил вещи на столе...")
#     print(f"[Статус] Загрузка завершилась? {download_task.done()}")
#     final_result = await download_task
#     print(f"[Итог]: {final_result}")
#     return final_result
#
# async def main():
#     await asyncio.gather(
#         main_task_1(),
#         main_task_2()
#     )
# asyncio.run(main())

# Задача 3
import asyncio

async def cook_dish(name, duration, fail=False):
    await asyncio.sleep(duration) #time.sleep()
    if fail:
        raise RuntimeError('Блюдо сгорело')
    return f'{name} готов'

async def main():
    print('Задача 3')
    # return_exceptions=True позволит не прерывать выполнение при ошибке
    results = await asyncio.gather(
        cook_dish('Салат', 1, fail=False),
        cook_dish('Запеканка', 2, fail=True),
        cook_dish('Компот', 3, fail=False),
        return_exceptions=True
    )
    for r in results:
        if isinstance(r, Exception):
            print(f'Ошибка: {r}')
        else:
            print(f'Успех: {r}')

# asyncio.run(main())


# ЗАДАЧА 4
async def alarm_clock():
    try:
        await asyncio.sleep(10)
        print('[Будильник] Пора вставать!')
    except asyncio.CancelledError:
        print('[Будильник] отменен пользователем')
        raise # проброс исключения для корректного завершения

async def main_alarm():
    print('Задача 4')
    task = asyncio.create_task(alarm_clock())
    print('[Я] сплю')
    await  asyncio.sleep(3)
    print('[Я] проснулся раньше')
    task.cancel()
    try:
        await task # ожидаем завершения корутины после отмены
    except asyncio.CancelledError:
        print('[Система] фоновая задача успешно и безопасно закрыта')

asyncio.run(main_alarm())




# print(isinstance(5, int))
