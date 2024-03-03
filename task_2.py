from collections import deque

def is_palindrome(s):
    # Перетворюємо рядок до нижнього регістру і видаляємо всі пробіли
    s = ''.join(s.lower().split())
    
    # Створюємо двосторонню чергу з символів рядка
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        # Порівнюємо і видаляємо символи з обох кінців
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True
