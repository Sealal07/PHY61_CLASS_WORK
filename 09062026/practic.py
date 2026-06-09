# Задача 1
# import asyncio
# import time
#
# async def water_flower(name, duration):
#     print(f"[Полив] Начинаю поливать {name}...")
#     await asyncio.sleep(duration)
#     print(f"[Полив] {name} успешно полит!")
#     return f"{name} готов"
#
# async def main_task_1():
#     print("Задача 1")
#     start_time = time.time()
#     results = await asyncio.gather(
#         water_flower("Фикус", 2), water_flower("Кактус", 1), water_flower("Орхидея", 3)
#     )
#     end_time = time.time()
#     total_time = end_time - start_time
#     print("результаты:", results)
#     print(f"время выполнения: {total_time:.2f} сек. (ожидалось около 3 секунд)")
#
# # Задача 2
# async def download_update():
#     for i in range(1, 5):
#         await asyncio.sleep(1)
#         print(f"[Загрузка] Скачано {i * 25}%...")
#     return "Обновление установлено"
#
#
# async def main_task_2():
#     print("Задача 2")
#     download_task = asyncio.create_task(download_update())
#     await asyncio.sleep(2)
#     print("[Я] Разложил вещи на столе...")
#     print(f"[Статус] Загрузка завершилась? {download_task.done()}")
#     final_result = await download_task
#     print(f"[Итог]: {final_result}")
#
#
#
# async def main():
#         await main_task_1()
#         await main_task_2()
#
# asyncio.run(main())


import asyncio
import time

async def water_flower(name, duration):
    print(f"[Полив] Начинаю поливать {name}...")
    await asyncio.sleep(duration)
    print(f"[Полив] {name} успешно полит!")
    return f"{name} готов"

async def download_update():
    for i in range(1, 5):
        await asyncio.sleep(1)
        print(f"[Загрузка] Скачано {i * 25}%...")
    return "Обновление установлено"

async def main_task_1():
    print("Задача 1")
    start_time = time.time()
    results = await asyncio.gather(
        water_flower("Фикус", 2),
        water_flower("Кактус", 1),
        water_flower("Орхидея", 3)
    )
    end_time = time.time()
    total_time = end_time - start_time
    print("результаты:", results)
    print(f"время выполнения: {total_time:.2f} сек. (ожидалось около 3 секунд)")
    return results

async def main_task_2():
    print("Задача 2")
    download_task = asyncio.create_task(download_update())
    await asyncio.sleep(2)
    print("[Я] Разложил вещи на столе...")
    print(f"[Статус] Загрузка завершилась? {download_task.done()}")
    final_result = await download_task
    print(f"[Итог]: {final_result}")
    return final_result

async def main():
    await asyncio.gather(
        main_task_1(),
        main_task_2()
    )
asyncio.run(main())