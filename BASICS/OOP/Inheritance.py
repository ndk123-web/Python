# Inheritance

class parent1:
    def featur1(self):
        print("Feature 1 from parent 1")

class parent2:
    def featur2(self):
        print("Feature 2 from parent 2")

class child(parent1,parent2):
    def greet(self):
        super().featur1()            
        super().featur2()
    
child1 = child()
child1.featur1()
child1.featur2()

child2 = child()
child2.greet()


# Inheritanace