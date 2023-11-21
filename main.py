import numpy as np

# функция активации нейрона (сигмоида)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def d_sigmoid(x):
    f = sigmoid(x)
    return f * (1 - f)

# вычисление среднеквадратической ошибки
def mse(y_true, y_pred):
    return ((y_true-y_pred)**2).mean()

# Нейрон
class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights # веса связей (входов)
        self.bias = bias # смещение

    # считаем вход
    def feedforward(self, inputs):
        # np.dot вычисляет скалярное произведение
        total = np.dot(self.weights, inputs) + self.bias # x1*w1 + x2*w2 + bias
        # применяем функцию активации
        return sigmoid(total)

# Класс нейросети
class NeuroNet:
    def __init__(self):
        # # нейроны скрытого слоя
        # self.h1 = Neuron(weights=np.random.normal(), bias=np.random.normal())
        # self.h2 = Neuron(weights=np.random.normal(), bias=np.random.normal())
        # # выходной нейро
        # self.o1 = Neuron(weights=np.random.normal(), bias=np.random.normal())
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feed_forward(self, x):
        # прямой проход по скрытому слою
        # out_h1 = self.h1.feedforward(x)
        # out_h2 = self.h2.feedforward(x)
        # # прямой проход выходного нейрона
        # out_o1 = self.o1.feedforward(np.array([out_h1, out_h2]))
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        o1 = sigmoid(self.w5 * x[0] + self.w6 * x[1] + self.b3)

        return o1

    # метод тренировки сети
    def train(self, data, all_y_true):
        # максимальное количество итераций обучения
        epochs = 1000
        # допустимая (желаемая) погрешность
        rate = 0.1

        for epoch in range(epochs):
            for x, y in zip(data, all_y_true):
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)
                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)
                sum_o1 = self.w5 * x[0] + self.w6 * x[1] + self.b3
                o1 = sigmoid(sum_o1)

                y_pred = o1


                # вычисление частных производных
                dld_yprep = -2 * (y_true - y_pred)

                # o1
                d_ypred_w5 = h1 * d_sigmoid(sum_o1)
                d_ypred_w6 = h2 * d_sigmoid(sum_o1)
                d_ypred_b3 = d_sigmoid(sum_o1)
                d_ypred_h1 = self.w5*d_sigmoid(sum_o1)
                d_ypred_h2 = self.w6*d_sigmoid(sum_o1)

                # h1
                d_ypred_w1 = x[0] * d_sigmoid(sum_h1)
                d_ypred_w2 = x[1] * d_sigmoid(sum_h1)
                d_ypred_b1 = d_sigmoid(sum_h1)

                # h2
                d_ypred_w3 = x[0] * d_sigmoid(sum_h2)
                d_ypred_w4 = x[1] * d_sigmoid(sum_h2)
                d_ypred_b2 = d_sigmoid(sum_h2)

                # обновление весов и смещения
                #h1
                self.w1 -= rate*dld_yprep*d_ypred_w1*d_ypred_h1
                self.w2 -= rate*dld_yprep*d_ypred_w2*d_ypred_h1
                self.b1 -= rate*dld_yprep*d_ypred_b1*d_ypred_h1

                # h2
                self.w3 -= rate * dld_yprep * d_ypred_w3 * d_ypred_h2
                self.w4 -= rate * dld_yprep * d_ypred_w4 * d_ypred_h2
                self.b2 -= rate * dld_yprep * d_ypred_b2 * d_ypred_h2

                # o1
                self.w5 -= rate * dld_yprep * d_ypred_w5
                self.w6 -= rate * dld_yprep * d_ypred_w6
                self.b3 -= rate * dld_yprep * d_ypred_b3

# создаем нейросеть
network = NeuroNet()

y_true = np.array([1, 0, 0, 0])
y_pred = np.array([0, 0, 0, 0])
print(mse(y_pred=y_pred, y_true=y_true))
