# class example
class A:
	def f(self):
		return self.g()
		
	def g(self):
		return 'A'
			
class B(A):
	def g(self):
		return 'B'

# Repl:
   a = A()
   a
=> <A object at 0x7fdc9d7d6f60>
   b = B()
   b
=> <B object at 0x7fdc9d7dae10>
   a.f
=> <bound method A.f of <A object at 0x7fdc9d7d6f60>>
   b.f
=> <bound method A.f of <B object at 0x7fdc9d7dae10>>
   a.g
=> <bound method A.g of <A object at 0x7fdc9d7d6f60>>
   b.g
=> <bound method B.g of <B object at 0x7fdc9d7dae10>>
