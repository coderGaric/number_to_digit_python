from click import clear
from art import logo, bye


class App:
    def reduce_to_digit(self, n):
        result = n
        while result >= 10:
            result = sum(int(digit) for digit in str(result))    
        return result

    def on(self):
        print(logo)

        is_reduce = False
        while not is_reduce:
            try:
                print("\n" + "-" * 50 + "\n")
                number = int(input("Enter number: "))
            except ValueError:
                print("Number only!!!")
            else:
                print("\n")
                if number >= 10:
                    digit = self.reduce_to_digit(number)
                    print(f"From {number} reduce to {digit}")
                else:
                    print("Nothing to reduce. IT'S A DIGIT")
                    
                print("\n" + "-" * 50 + "\n")
                
                to_continue = input("'y' to continue | any key to exit: ").lower()

                clear()
                
                if to_continue == "y":
                    print(logo)
                    continue
                else:
                    print(bye)
                    is_reduce = True


numbers_to_digit = App()
numbers_to_digit.on()