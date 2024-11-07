#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
  

    
# txt = "[name]" x = txt.replace("[name]", f.readlines(i))
# txt =  "        banana     "  x = txt.strip()   print("of all gfuits", x, "is my favourite")




names = open("./Input/Names/invited_names.txt", "r")
x = (names.readlines())


    
with open("./Output/ReadyToSend/example.txt", "r") as file:
    content = file.read()

with open("./Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()
    
    

 
letters = []


for name in x:
    new_name = name.strip("\n")
    new_letter = (starting_letter.replace("[name]", new_name))
    letters.append(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as file:
        file.write(new_letter)
print(letters)




 
