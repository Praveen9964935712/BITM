class Box:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
class Box2(Box):
    def __init__(self,name,roll,marks):
        self.marks=marks
        # student.__init__(self,fees)
        Box.__init__(self,name,roll)

obj=Box2("sneha",12,23)
print(obj.name)
print(obj.roll)
print(obj.marks)