class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        # хранение подходящих комбинаций
        result = []

        # start - число, с которого начнем перебор
        # current - комбинация, которую собираем прямо сейчас
        # current_sum - сумма чисел в current
        def backtracking(start, current, current_sum):

            # проверка, есть ли в текущей комбинации k чисел нужная сумма

            if len(current) == k:
                if current_sum == n:
                    result.append(current.copy())
                return

        # если сумма стала слишком большой, дальше идти смысла нет
            if current_sum >= n:
                return


            for num in range(start, 10):
            # пробуем добавить число в комбинацию
                current.append(num)

            # идем глубже и подбираем следующие числа
            # num + 1 означает, что это же число повторно добавлять нельзя
                backtracking(num + 1, current, current_sum + num)

            # пробуем убрать последнее число, чтобы попробовать другой вариант
                current.pop()

        # сначала начинаем с 1, комбинация пустая, сумма 0
        backtracking(1, [], 0)

        return result


#     также возможно решение через from itertools import combinations, 
#     но задача на бэктрэкинг
