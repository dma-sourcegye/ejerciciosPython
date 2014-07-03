from os import system
i=0
op=""

class Postre:
	def __init__(self,nombre):
		self.nombre=nombre
		print nombre

	def Ingrediente(self,nombre,indice):
		self.nombre=nombre
		self.indice=indice
		print nombre+": ", indice


while op!="n":
	system("cls")
	i+=1
	nom=raw_input("Ingrese el nombre del postre: ")
	nom2=raw_input("ingrese el ingrediente: ")
	postre=Postre(nom)
	postre.Ingrediente(nom2,i)
	op=raw_input("Desea Continuar (s/n): ")
