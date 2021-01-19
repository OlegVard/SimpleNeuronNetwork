from Neuron_class import Network
import time

print('Введите количество долларов')
dollar = int(input())
euro = 0.8258

start_time = time.time()

net = Network()
result = net.train(1, euro)
result = result * dollar
print('в', dollar, 'долларах', round(result, 2), 'евро')
end_time = time.time()
print('Время выполнения в секундах =', end_time - start_time)
