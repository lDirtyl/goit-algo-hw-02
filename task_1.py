"""
import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
"""

import queue
import time
import threading

# Створити чергу заявок
request_queue = queue.Queue()

def generate_request(request_id):
    """Створює нову заявку і додає її до черги"""
    request = f"Заявка {request_id}"
    request_queue.put(request)
    print(f"Додано до черги: {request}")

def process_request():
    """Обробляє заявку з черги"""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Оброблено: {request}")
    else:
        print("Черга пуста")

def main():
    request_id = 1

    # Імітація роботи програми: створюємо і обробляємо заявки
    while True:
        # Генеруємо нову заявку
        generate_request(request_id)
        request_id += 1

        # Імітація затримки для обробки заявок
        time.sleep(1)

        # Обробляємо заявку
        process_request()

        # Імітація затримки перед наступною ітерацією
        time.sleep(1)

        # Умова виходу для демонстрації (після 10 заявок)
        if request_id > 10:
            break

if __name__ == "__main__":
    main()
