# Topic 19: Inheritance

# Questions
# 1. What are types of inheritance?
# 2. What is Method Resolution Order (MRO)?

# Notes
# Types: Single, Multiple, Multilevel, Hierarchical, Hybrid
# MRO: Order in which methods are resolved

# Solutions
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
c = C()
c.show()
print(C.__mro__)
