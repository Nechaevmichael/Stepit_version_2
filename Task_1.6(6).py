# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# журавликов, чем Петя и Сережа вместе?
# Входные данные
# Поступает одно натуральное число S – общее количество сделанных журавликов.
# Выходные данные
# В единственную строку нужно вывести три числа, разделенных пробелами – количество журавликов, которые сделал каждый
# ребенок (Петя, Катя и Сережа).

S = int(input())
P = S // 6
C = S // 6
K = (P + C) * 2
print(P, K, C)