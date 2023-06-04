
# �������� ���������� ��������� �� �����
def sort(nums):
  for  i in range(len(nums)):
      for j in range(len(nums)-i-1):
          if nums[j] > nums[j+1]:
              nums[j], nums[j+1] = nums[j+1], nums[j]

  print("�������������")
  return nums
  
# ������� ��������� ������ �� �����
def binary_search(array, element, left, right): 
    if left > right: # ���� ����� ������� ��������� ������,
        return False # ������ ������� �����������
    
    middle = (right+left) // 2 # �������� ��������
    if array[middle] == element: # ���� ������� � ��������,
        return middle # ���������� ���� ������
    elif element < array[middle]: # ���� ������� ������ �������� � ��������
        # ���������� ���� � ����� ��������
        return binary_search(array, element, left, middle-1)
    else: # ����� � ������
        return binary_search(array, element, middle+1, right)
 

print("������� ����� ����� ������")
s=input()
array = s.split() #��������� ������ �� ������
nums = [int(x) for x in array] #����� ������ ��������� �� ����


#��� ���� ���������� ���������
print("�������� ���������� ������")
sort(nums)
print(nums)


#����� � ������
searchNum = int(input("������� ����� ��� ������ � �������� ������������������ \n"))

if searchNum in nums: #��������� ���� �� ����� � ������
  print("�����", searchNum, "����� ��", binary_search(nums, searchNum, 0, len(nums))+1, "�����")
else:
  print("� ���� ������������������ ��� ������ �����")


print(nums)