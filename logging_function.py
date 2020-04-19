class Logging_Function():

    x = '5'

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def test_log(self):

        print('method inside class!')


    def test_name(self, name, city):
        return self.name + self.city + Logging_Function.x



obj = Logging_Function.test_name(5, 6)
print(obj)


