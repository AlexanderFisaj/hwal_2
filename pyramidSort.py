# Задача. Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

from random import randint

def heapify(array, heapSize, rootIndex):
    largestElement = rootIndex  
    leftСhild = 2 * rootIndex + 1     
    rightChild = 2 * rootIndex + 2     
 
    if leftСhild < heapSize and array[rootIndex] < array[leftСhild]:
        largestElement = leftСhild
 
    if rightChild < heapSize and array[largestElement] < array[rightChild]:
        largestElement = rightChild
 
    if largestElement != rootIndex:
        array[rootIndex],array[largestElement] = array[largestElement],array[rootIndex]  
        heapify(array, heapSize, largestElement)
 
def heapSort(unsortArrey):
    n = len(unsortArrey)
 
    for i in range(n, -1, -1):
        heapify(unsortArrey, n, i)
 
    for i in range(n-1, 0, -1):
        temp = unsortArrey[i]
        unsortArrey[i] = unsortArrey[0]
        unsortArrey[0] = temp
        heapify(unsortArrey, i, 0)
 
unsortArray = [randint(10, 100) for _ in range(20)]
print(f'\nНеотсортированный: {unsortArray}\n')
heapSort(unsortArray)
n = len(unsortArray)
print (f'Отсортированный: {unsortArray}\n')
