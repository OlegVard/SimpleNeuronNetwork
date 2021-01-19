import random
import math


class Network:
    weight = [0.4, 0.6, 0.3, 0.5, 0.9, 0.2]

    def train(self, dol, ev):
        weight = self.weight
        for i_iter in range(100000):
            weight_h1 = dol * weight[0]
            act1 = self.activate(weight_h1)
            weight_h2 = dol * weight[1]
            act2 = self.activate(weight_h2)
            weight_h3 = dol * weight[2]
            act3 = self.activate(weight_h3)
            weight_out = act1 * weight[3] + act2 * weight[4] + act3 * weight[5]
            act_out = self.activate(weight_out)
            if act_out != ev or act_out < 1.2102230246251565e-16:
                error = ev - act_out
                correction = error/act_out
                weight[5] = weight[5] + correction * weight_out * (1 - act_out)
                weight[4] = weight[4] + correction * weight_out * (1 - act_out)
                weight[3] = weight[3] + correction * weight_out * (1 - act_out)
                weight[2] = weight[2] + correction * act3 * (1 - act3)
                weight[1] = weight[1] + correction * act2 * (1 - act2)
                weight[0] = weight[0] + correction * act1 * (1 - act1)
                print(i_iter + 1, 'итерация. Ошибка =', error)
            else:
                print('Нейросеть обучена')
                return act_out

    def activate(self, x):
        return 1 / (1 + math.exp(-x))
