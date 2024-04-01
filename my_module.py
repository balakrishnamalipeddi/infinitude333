class student():

    desgination = "software engineer"
    def __init__(self,name,age):
       self.name = name
       self.age = age

    @staticmethod
    def add(x,y):
        return x+y


    def test(self):
        print("student name is "   +  self.name , "age is "  +  self.age, "desgination is" + self.desgination)
    @classmethod
    def new_test(cls):
        cls.desgination = "Tester"
        print("This is class method" + cls.desgination)


obj = student("balu ",  "25")
obj2 = student("usha", "26")

obj.new_test()
print(student.desgination)

print(student.add(5,3))

