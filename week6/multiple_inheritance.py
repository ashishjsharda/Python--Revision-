class Father:
    def skills(self):
        print("Father's skills: Fishing, Hunting")
        
class Mother:
    def skills(self):
        print("Mother's skills: Cooking, Gardening")

class Child(Father, Mother):
    def skills(self):
        print("Child's skills: Programming, Painting")
        Father.skills(self)
        Mother.skills(self)
        

c= Child()
c.skills()
