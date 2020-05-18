'''
Even-Odd Vending Machine
1. Print whether the number is even or odd.
2. Display the number followed by the next 9 even or odd numbers.
'''

def even_odd_vending():
    try:
        a = float(input("Enter an number: "))
        
        if a.is_integer():
            for i in range(9):
                print(a + i * 2, end = ", ")
        else:
            print("a is not an integer.")
            
    except ValueError:
        print("Please input a number!")

    

if __name__ == "__main__":
    even_odd_vending()
