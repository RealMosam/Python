class ei:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        real = self.real + other.real
        img = self.img + other.img
        ans = ei(real,img)
        return ans

    def __sub__(self, other):
        real = self.real - other.real
        img = self.img - other.img
        ans = ei(real, img)
        return ans


obj1 = ei(float(input("Enter Real No.")),float(input("Enter Imaginary No.")))
obj2 = ei(float(input("Enter Real No.")),float(input("Enter Imaginary No.")))
ans = obj1 + obj2
print("The add operator overloading is:")
print(ans.real,"+","j",ans.img)

ans = obj1 - obj2
print("The sub operator overloading is:")
print(ans.real,"-","j",ans.img)





