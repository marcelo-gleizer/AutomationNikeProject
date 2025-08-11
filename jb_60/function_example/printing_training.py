from jb_60.function_example.utils import utils
utils_instance=utils()
num3 = 3
num4 = 6
new_print_num = utils_instance.print_num(num3, num4)

array=[2,3,8]
array_length=len(array)
array_sum=sum(array)
result = array_sum/array_length
print(result)