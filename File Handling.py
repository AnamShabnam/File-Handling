file_name = "D:\\myfile.text"

choice = input("please enter any number (w/r): ")

if choice == "1":
         file = open(file_name, "w")
         text = input("Enter text to write to the file: ")
         file.write(text)
         print("{text} was written to {file_name}.")
elif choice == "2":
         file = open(file_name, "a")
         text = input("Enter text to write to the file: ")
         file.append(text)
         print("{text} was append to {file_name}.")
elif choice == "3":
       file = open(file_name, "r")
       contents = file.read()
       print("The contents of {file_name} are: {contents}")
else:
       print("Error: {file_name} does not exist.")






