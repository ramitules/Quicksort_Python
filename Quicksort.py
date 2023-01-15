def partition(array, low, high):
	
	# Capturar el elemento mas a la derecha
	pivot = array[high]

	# Puntero del elemento mas grande
	i = low - 1

	# Iterar a traves de todos los elementos y buscar los mas grandes
	for j in range(low, high):
		if array[j] <= pivot:
			# Si el elemento es mas chico que el pivot,
			# cambiarlo por el elemento mas grande
			i = i + 1

			# Cambiar elemento en i con elemento en j
			(array[i], array[j]) = (array[j], array[i])

	# Cambiar elemento pivot por elemento mas grande en puntero i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Retornar la posicion desde donde la particion es hecha
	return i + 1


# Funcion principal de Quicksort
def quick_sort(array, low, high):
	if low < high:

		# Encontrar elemento pivot tal que
		# elemento mas pequeno que el pivot va a la izquierda
		# elemento mas grande que el pivot va a la derecha
		pi = partition(array, low, high)

		# Recursion a la izquierda del pivot
		quick_sort(array, low, pi - 1)

		# Recursion a la derecha del pivot
		quick_sort(array, pi + 1, high)


# Codigo ejemplo
array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)

print(f'Vector ordenado: {array}')
