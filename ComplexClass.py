import math

def main():
    # x is first complex number
    # y is second complex number

    x_real, x_imaginary = read_input()  # store values for x set of complex numbers
    y_real, y_imaginary = read_input()  # store values for y set of complex numbers

    x = complex(x_real, x_imaginary)
    y = complex(y_real, y_imaginary)

    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print("{:.2f} + 0.00i".format(x.modulus()))
    print("{:.2f} + 0.00i".format(y.modulus()))


def read_input():
    while True:
        try:
            real = float(input("Enter a number: "))
            imaginary = float(input("Enter a second number: "))

            if real is None or imaginary is None:  # check to see if either of the values are 0.
                raise ValueError
            
            return real, imaginary
            
        except ValueError:
            print("Invalid input.")


class complex(): 
    
    def __init__(self, real, imaginary):
        # will allow the initilization of an instance of the Complex class. it is a constructor method.
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):  # this name allows us to use the + operator for this method
        sum_for_real = self.real + other.real  # add both the real parts
        sum_for_imaginary = self.imaginary + other.imaginary  # add both the imaginary parts
        return complex(sum_for_real, sum_for_imaginary)  # returns the sum of the real and imaginary parts

    def __sub__(self, other):  # this name allows us to use the - operator for this method
        diff_for_real = self.real - other.real  # subtract both the real parts
        diff_for_imaginary = self.imaginary - other.imaginary  # subtract both the imaginary parts
        return complex(diff_for_real, diff_for_imaginary)  # returns the difference of the real and imaginary parts

    def __mul__(self, other):  # this name allows us to use the * operator for this method
        # a complex number is in the form (a + bi). if we want to multiply two complex numbers
        # we need to take the form (a + bi)(c + di) and use the distributive propery.
        # ac + adi + bci + bdi^2. Keep in mind i^2 = -1
        # (ac - bd) + i(ad + bc)
        # self.real = a, self.imaginary = b, other.real = c, other.imaginary = d
        mult_real = self.real * other.real - self.imaginary * other.imaginary  # multiply real
        mult_imaginary = self.real * other.imaginary + self.imaginary * other.real  # multiply imaginary
        return complex(mult_real, mult_imaginary)  # returns the multiplication of the real and imaginary parts
    
    def __truediv__(self, other):  # this name allows us to use the / operator for this method
        # to divide (a + bi)/(c + di), the formula is ((a + bi) * (c - di))/c^2 + d^2
        # distributive propery: (ac + bd) + (-ad +bc)i
        # self.real = a, self.imaginary = b, other.real = c, other.imaginary = d
        denominator = other.real ** 2 + other.imaginary ** 2
        divide_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        divide_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return complex(divide_real, divide_imaginary)
    
    def modulus(self):
        # modulus of a complex number is sqrt(a^2 + b^2)
        # self.real = a, self.imaginary = b, other.real = c, other.imaginary = d
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5 # anything to the power of 0.5 is just square root 
    
    def __str__(self):  # overrides the string representation to be as follows. reflected when used with print statement.
        # .3f makes the float (f) accurate to three decimal places. The colon is the format specification
        return "{:.2f} {:+.2f}i".format(self.real, self.imaginary).replace(" +", " + ").replace(" -", " - ")
    
if __name__ == "__main__":  # make the main method the main method
    main()