import random

class A:


    a = 3
    b = 4

    # @staticmethod
    def sum(self):
        return self.a + self.b


if __name__ == '__main__':
    # x = float('{:.2f}'.format(random.randint(1000, 2000) * 0.01))
    x = '{:.2f}'.format(random.randint(1000, 2000) * 0.01)

    print(x)