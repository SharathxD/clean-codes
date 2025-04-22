import extra as ex

print("Checking imports")
print("----------------------------")
print(ex.file_name())
answer=ex.add(34,35)
print(f"addition function imported {answer}")
print(f"Subtration function imported {ex.subtract(100,0)}")
print(f"Multiplication function imported {ex.multiply(4,4)}")
print(f"Division function imported {ex.divide(100,10)}")
print(f"Power function imported {ex.power(2,3)}")
print("----------------------------")

print("checking the class imports ")
print("==============================")


import oops as op
C1=op.Car()
C1.name("BMW")
C1.display()
C1.addType("EV")
