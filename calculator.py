def add(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
    
def sub(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result-=num
    return result

def mul(numbers):
    result=1
    for num in numbers:
        result*=num
    return result

def div(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            return "error/not divisible by zero"
        result/=num
    return result



def calculator():
    print('<-----Calculator-----.')
    print('1. Add')
    print('2. subtract')
    print('3. multiply')
    print('4. divide')
    print("5. Exit")

    while True:

        choice=(input("enter the choice: "))

        if choice in ('1','2','3','4','5'):
            if choice=='5':
                print("exiting.....")
                break
            n=int(input("enter the number of elements: "))
            numbers=[]
            for i in range(n):
                num=int(input(f"enter the number{i+1}: "))
                numbers.append(num)
            
            if choice=='1':
                print(f"result: {add(numbers)}")

            elif choice=='2':
                print(f"result: {sub(numbers)}")

            elif choice=='3':
                print(f"result: {mul(numbers)}")

            elif choice=='4':
                print(f"result: {div(numbers)}")

            elif choice=='5':
                print("exiting......")
                break

            a=input("Do you want to perform another operation(yes/no)")
            if a!='yes':
                break

        else:
            print("invalid input")

calculator()



    
    

    
        
        
        
            
        

        

        

        


        
    
        

    

