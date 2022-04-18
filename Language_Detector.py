from langdetect  import detect
while True:

    text=input("Enter the Setence:-")
    print(detect(text))