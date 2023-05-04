class Clothing:
  material = ""
  def __init__(self,name):# constructor
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):# inherited class from the base class clothing
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

class pants(Clothing):
    material="rayon"

jeans = pants("jeans")
jeans.checkmaterial()
