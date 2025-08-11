from tkinter.font import names


class utils:


        def getting_vat(self,price):
            print (f"Getting VAT for {price}")
            new_price = price.replace("$","")
            new_price_as_int = int(new_price)
            new_price_final = new_price_as_int * 1.18
            print(f" the final price is {new_price_final}")
            return new_price_final

        def add_suffix(self, price,rate):
            price = price*rate
            price_as_str= str(price) # changing the variable value form float to string
            new_price = price_as_str+"ILS"
            print(f"the price is {new_price}")

        def avg_calc(self,nums):
            print("calculate Avg. of numbers")
            sum =0
            for num in nums:
                print(num)
                sum = sum + num

            size = len(nums)
            avg = sum/size
            print(f"the avg value is {avg}")

        def getting_avg(self, num1, num2):
            avg = (num1 + num2) /2
            print(f" the avg is {avg}")
            return avg , size

        def print_num(self, num1, num2):
            if num1 > num2:
                while (num2<num1 - 1):
                    num2 += 1
                    print(num2)
            else:
                while (num1<num2 - 1):
                    num1 += 1
                    print(num1)

        def print_name(self, arr):
            longest_name = ""
            for name in arr:
                if len(name) > len(longest_name):
                    longest_name= name
            return longest_name


