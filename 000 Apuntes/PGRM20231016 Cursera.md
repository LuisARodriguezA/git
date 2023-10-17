2023-10-16
12:28:36
Tags: #PGRM #UNAL #Python
___
# PGRM20231016 Cursera
___
## More String Methods
* When dealing with user input dont expect the user to input exactly what you need, just change it.
```run-python 
answer = 'YES'
if answer.lower() == "yes":
	print("User said yes")
	
```
* Strip methoth
	* Get rid of everything around a specific point in the string
	* Removes everything else that is awfull
```run-python
print(" yes ".strip( ))
print(" yes ".lstrip( ))
print(" yes ".rstrip( ))
```
* **count** returns how many times a given character or string apears.
* **endwith** well, tells  you that
* **isnumeric** well...
	* We can use de int function then
* joint method is use to concatenate
* call it on the string that will be use to do the joining.
* split() turns a list of all the individual words, o you can pass a parameter to split in a specific character.
## Formatting Strings
* format method
```run-python
name = "Manny"
number = len(name) * 3

print("Hello {}, your lucky number is {}".format(name,number))

print("Hello {name}, your lucky number is {number}".format(name=name, number=len(name) * 3))
```
* It dosen't matter if it is a str or a int
``` run-python
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
```
___
# Todo
- [ ] 
___
# Sources
1. 
___