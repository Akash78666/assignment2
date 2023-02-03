n=int(input("please in the Glucose:\n"))
def my_Glucose(n):

    if n==350:
        print("Your Glucose is v.High. take a bed rest")
    elif n>=150:
        print("Your Glucose is High. to advice to walk in the morning")
    elif n>=90:
        print("Your  Glucose is normal.to take eaten healthy diet")
    elif n<90:
        print("Your  Glucose is low becaue your sufferend anxiety.join us happy grourp")
    else:
        print("your the healthy person.don't prescrible medicine")
my_Glucose(n)      
