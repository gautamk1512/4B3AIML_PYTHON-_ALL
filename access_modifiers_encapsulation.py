# Topic 22: Access Modifiers and Encapsulation

# Questions
# 1. What is encapsulation?
# 2. What are access modifiers?
# 3. What is the difference between public, private, and protected?

# Notes
# Encapsulation: Bundling data and methods
# Access modifiers: public (_), protected (_var), private (__var)

# Solutions
class Test:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"
    def show(self):
        print(self.public)
        print(self._protected)
        print(self.__private)
t = Test()
t.show()
