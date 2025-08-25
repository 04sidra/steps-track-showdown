import pandas as pd
import matplotlib.pyplot as plt 
import os

def register_student():
    print(" Student Registration ")

    name=input("enter the name:")
    age=input("enter the age:")
    weight=input("enter the weight:")
    place=input("enter the place:")
    steps=input("enter steps completed in 45 minutes:")
    data=pd.DataFrame([[name,age,weight,place,steps]],columns=["Name","Age","weight","place","steps"])
    file=os.path.isfile("student.csv")
    data.to_csv("student.csv",mode="a",index=False,header=not file)
    print("Registration successfull")

def show_chart():
    df=pd.read_csv("student.csv")
    plt.bar(df["Name"],df["steps"])
    plt.xlabel("student name")
    plt.ylabel("steps completed in 45 minutes")
    plt.title("Students Fitness")
    plt.show()
def graph():
    df=pd.read_csv("student.csv")
    df["steps"]=pd.to_numeric(df["steps"],errors="coerce")
    plt.pie(df["steps"],labels=df["Name"],autopct="%1.1f%%")
    plt.title("students fitness")
    plt.show()

while True:
    print("\n......Student Registration........")
    print("1.Register student")
    print("2.show chart")
    print("3.graph")
    print("4.Exit")
    choice=input("enter your option:")
    if choice=="1":
        register_student()
    elif choice=="2":
        show_chart()
    elif choice=="3":
        graph()
    elif choice=="4":
        print("Goodbye! Have a wonderful day ahead ")  
        break
    else:
        print("Invalid choice,please try again.\n")  


    
