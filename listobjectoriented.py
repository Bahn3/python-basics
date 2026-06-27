# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def accelerate(self):
#         print('Vrooom')
# bug = Car('Bugatti')
# bug.accelerate()
# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def sit(self):
#         print('sit')
#     def bark(self):
#         print('bark')
#         print(f'My name is {self.name}')
# tuffy = Dog('Tuffy')
# maxx = Dog('Maxx')
# tuffy.sit()
# tuffy.bark()
# maxx.sit()
# maxx.bark()
class List:
    def __init__(self, list1):
        self.list1 = list1
    def multiply_list(self):
        initial = self.list1[0]
        for num in self.list1[1: ]:
            initial = initial*num
        return initial
def main():
    list1_num =[5,6,7]
    list2_num = [8,9,10]
    list1_result = List(list1_num)
    list2_result = List(list2_num)
    max1 = list1_result.multiply_list()
    max2 = list2_result.multiply_list()
    print(max(max1, max2))
main()
print('hello')