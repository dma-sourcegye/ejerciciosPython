from os import system
lista=[]#Lista principal
lista2=[]#lista donde se almacenaran los elementos inevrtidos
lista3=[] #pila que servirá para invertir los valores de la lista


def GenerarLista(lista,lista2,lista3):
	op=""
	while op!="n":
		system("cls")
		itemLista=int(raw_input("Ingrese un elemento: "))
		lista.append(itemLista)
		lista3.append(itemLista)
		op=raw_input("desea continuar (s/n): ")

	print "Elementos de la lista generada: ", lista
	for item in lista:
		lista2.append(lista3.pop())
	print "lista ivertida: ",lista2

	op=raw_input("Desa eliminar la lista (s/n)? ")
	if(op=="s"):
		del (lista)
		print "lista eliminada"
	else:
		print "no se elimino la lista"

GenerarLista(lista,lista2,lista3)
