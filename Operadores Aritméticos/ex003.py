from asyncio.windows_events import NULL
from selectors import SelectSelector

n1 = int(input('Digite o primeiro valor'))
n2 = int(input('Digite o segundo valor'))
soma = n1 + n2
print('A soma entre {} e {} é {}'.format(n1, n2, soma))