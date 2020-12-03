""""
program to reverse string - Random Codes Repository- Rohan Ganguly
""""
import string #importing the string library

#input the string into a variable string1
string1= input("Enter the string to reverse:")

#the split function to split the input string and save it as a list
#the list split contains the words of the input string
split= string1.split()

#use the reverse function to reverse the elements of the list
split.reverse()

#use the join function to join the elements of the list into a string
#a for loop using a temporary variable temp is used to traverse the list
reverse_string= " ".join([str(temp) for temp in split])

#print the value of the variable reverse_string
print(reverse_string)

