# Example of Hybrid Inheritance 
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass


# class BaseClass1:
#   # attributes and methods

# class BaseClass2:
#   # attributes and methods

# class DerivedClass(BaseClass1, BaseClass2):
#   # attributes and methods





# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass