# class parent:
#     def output(self):
#         print('I am parent')
# class child(parent):
#     def outputc(self):
#         print('i am child')

# c1=child()
# c1.output()
# c1.outputc()
# p=parent()
# p.output()

class grandfather:
    def outputgf(self):
        print('I am grandfather')
class parent(grandfather):
    def outputp(self):
        print('I am parent')
class child(parent):
    def outputc(self):
        print('i am child')

c1=child()
c1.outputc()
c1.outputp()
c1.outputgf()
