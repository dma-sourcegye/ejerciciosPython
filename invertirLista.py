from os import system
lista=[]#Lista principal
lista2=[]#lista donde se almacenaran los elementos invertidos
lista3=[] #pila que servira para invertir los valores de la lista


def InvertirLista(lista,lista2,lista3): #Funcion  inversora
	op=""
	while op!="n":
		system("cls") #limpia la pantalla de la consola se pasa como parametro cls si el script se ejecuta en windows
		itemLista=int(raw_input("Ingrese un elemento: ")) #se pide ingresar un elemento para nuestra lista el cual sera del tipo entero
		lista.append(itemLista) #se agrega el elemento a la lista
		lista3.append(itemLista)#se agrega el mismo element a la pila
		op=raw_input("desea continuar (s/n): ") #el script nos pregunta si deseamos continuar con el ingreso de elementos

	print "Elementos de la lista generada: ", lista #imprimimos todos los elementos del objeto lista
	for item in lista:
		lista2.append(lista3.pop()) #se almacenan lso elementos de manera invertida en una nueva lista
	print "lista ivertida: ",lista2     #presentamos la nueva lista

#como opcion nos dan a elegir si se desea eliminar la primera lista ya que esta no nos servira mas
	op=raw_input("Desa eliminar la lista (s/n)? ")
	if(op=="s"):
		del (lista) 	#eliminamos la lista
		print "lista eliminada"
	else:
		print "no se elimino la lista"

InvertirLista(lista,lista2,lista3)  	#llamamos a la funcion InvertirLista
