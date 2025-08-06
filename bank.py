greeting = input("Greeting:").lower().strip()

if greeting == "hello" or greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h" and greeting != "hello":
    print("$20")
else:
    print("$100")


          