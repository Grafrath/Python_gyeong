class calculator :
    def __init__(self, f, s):
        self.f = f
        self.s = s
    
    def add (self):
        result = self.f + self.s
        return result
    
    def sub (self):
        result = self.f - self.s
        return result
    
    def mul (self):
        result = self.f * self.s
        return result
    
    def div (self):
        if self.s != 0 :
            result = self.f / self.s
            return result
        else:
            print("0으로 나눌 수 없습니다.")
    
a = calculator(5,5)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class morecal(calculator):
    def pow (self):
        result = self.f ** self.s
        return result
    
    def div (self):
        if self.s == 0 :
            print("0 으로 나눌 수 없습니다.")
            return 0
        else:
            result = self.f / self.s
            return result
        
b = morecal(5,3)

print(b.pow())

b = morecal(5,0)
print(b.div())