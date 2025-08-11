from jb_60.function_example.utils import utils

utils_instance=utils()

cities = ["london", "Athen", "New-york", "Jerusalem", "Lod"]

value = utils_instance.print_name(cities)
print(f"the value found it {value}")