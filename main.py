from Neuron_class import Network

print('Введите количество долларов')
dollar = int(input())
euro = 0.8258

net = Network()
result = net.train(1, euro)
result = result * dollar
print('в', dollar, 'долларах', round(result, 2), 'евро')
