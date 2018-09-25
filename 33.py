print("Enter 'x' for exit.")
string = raw_input("Enter any string to remove all vowels from it: ")
newstr = string;
print("\nRemoving vowels from the given string...");
    #vowels = ('a', 'e', 'i', 'o', 'u');
for x in string:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        newstr = newstr.replace(x,"");
print("New string after successfully removed all the vowels:");
print(newstr);
