# Известно, что на обработку одного квадратного метра панели требуется 1г сульфида. Всего необходимо обработать N
# прямоугольных панелей размером A на B метров. Вам необходимо подсчитать, сколько всего сульфида необходимо
# на обработку всех панелей. И не забудьте, что панели требуют обработки с обеих сторон.
# На вход программе подаются 3 положительных целых числа N,A,B в одну строку

N, A, B = map(int, input().split())
print(2 * N * (A * B))