import numpy as np


class MinMaxScaler:
    minimum = np.array([])
    maximum = np.array([])

    def fit(self, data):
        self.maximum = np.max(data, axis=0)
        self.minimum = np.min(data, axis=0)

    def transform(self, data):
        data = data.T
        for i in range(len(data)):
            if self.maximum[i] != self.minimum[i]:
                data[i] = (data[i] - self.minimum[i]) / (self.maximum[i] - self.minimum[i])
            else:
                data[i] = 0
        return data.T


class StandardScaler:
    sigm = np.array([])
    EM = np.array([])

    def fit(self, data):
        self.EM = np.mean(data, axis=0)
        self.sigm = np.std(data, axis=0)

    def transform(self, data):
        data = data.T
        for i in range(len(data)):
            if self.sigm[i] != 0:
                data[i] = (data[i] - self.EM[i]) / self.sigm[i]
            else:
                data[i] = 0
        return data.T
