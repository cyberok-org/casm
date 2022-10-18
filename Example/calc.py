

print('TS минимальноо штрафа')
g = float(input())
print('Минимальный штраф')
a = int(input())

print('TS gромежуточного штрафа')
gamma = float(input())
print('Промежуточгный штраф')
alpha = int(input())

print('Максимальный штраф')
c = int(input())


b = (gamma*(c-alpha) - g*(c-a))/(alpha-a)
k = (c-a)*(b+g)

print("b = " + str(b))
print("k = " + str(k))
