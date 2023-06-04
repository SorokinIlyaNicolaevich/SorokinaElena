
# алгоритм сортировки пузырьком из курса
def sort(nums):
  for  i in range(len(nums)):
      for j in range(len(nums)-i-1):
          if nums[j] > nums[j+1]:
              nums[j], nums[j+1] = nums[j+1], nums[j]

  print("ќтсортировано")
  return nums
  
# алгорим бинарного поиска из курса
def binary_search(array, element, left, right): 
    if left > right: # если лева€ граница превысила правую,
        return False # значит элемент отсутствует
    
    middle = (right+left) // 2 # находимо середину
    if array[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle-1)
    else: # иначе в правой
        return binary_search(array, element, middle+1, right)
 

print("¬ведите числа через пробел")
s=input()
array = s.split() #раздел€ем строку на список
nums = [int(x) for x in array] #делам список состо€щий из цифр


#“ут идет сортировка пузырьком
print("запущена сортировка списка")
sort(nums)
print(nums)


#ѕоиск в списке
searchNum = int(input("¬ведите число дл€ поиска в веденной последовательности \n"))

if searchNum in nums: #провер€ем есть ли число в списке
  print("„исло", searchNum, "стоит на", binary_search(nums, searchNum, 0, len(nums))+1, "месте")
else:
  print("¬ этой последовательности нет такого числа")


print(nums)