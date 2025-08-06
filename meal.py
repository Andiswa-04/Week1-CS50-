def main():
     n = convert(input("Please enter time in 24-hour format : "))
    

     if 7 <= n <=8 :
          print('Breakfast time')
     elif 12 <= n <= 13 :
          print("Lunch time")
     elif 18 <= n <= 19 :
          print("Dinner")
     else :
          print("No you are not hungry")
        

def convert(time):
     time_split = time.split(":")
     hours = int(time_split[0])
     minutes = int(time_split[1])
     decimal_time = hours +(minutes / 60)
     return decimal_time 

if __name__ == "__main__":
    main()



     

       


