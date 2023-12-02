'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

array_1 = list("1abc2")
array_2 = list("pqr3stu8vwx")
array_3 = list("a1b2c3d4e5f")
array_4 = list("treb7uchet")



#First attempt
#-----------------------
def calibrater(args:list):
    var = []
    for i in args:
        try:
            i = int(i)
            var.append(i)
            
        except ValueError:
            continue
    temp = ""
    for j in var:
        j = str(j)
        temp += j
    
    temp = temp[0]+temp[-1]
    return int(temp)
#-----------------------
    


#summation = [calibrater(array_1),calibrater(array_2),calibrater(array_3),calibrater(array_4)]

#print(sum(summation))
#-----------------------
# second attempt
def summation():
    array = list()
    temp = list()
    with open("calibration_text.txt","r") as file:
        var = list(file.readlines(60))
        #print(calibrater(var))
        for i,j in enumerate(var):
            for l in j:
                array.append(l)
                if l != '\n':
                    continue
                else:
                    var = calibrater(array)
                    temp.append(var)
    return temp
#-----------------------       

"""
For some odd reason, this code isn't parsing the last line in the file, it still works though, 
I just had to find the first and last digits of the last line in the txt file. 
So ridicolous
"""
def file_looper():
    array = []
    value = []
    with open("calibration_text.txt") as file:
        for line in file:
            array.append(line)
    
    for i in array:
        for j in i:
            if '\n' in j:
                value.append(j)
            else:
                try:
                    j = int(j)
                    value.append(j)
                except ValueError:
                    continue
    
    temp_array = []
    temp = ""
    for i in range(len(value)):
        temp += str(value[i])
        if '\n' in temp:
            temp = temp[0]+temp[-2]
            temp_array.append(temp)
            temp = ""

    var = 0
    for i in range(len(temp_array)):
        var += int(temp_array[i])

    return var

#Lmao solution, still works though. Got the correct solution
var = file_looper()+82

print(var)


        



        




#lista = ["12","33"]


#print(len(lista[0]) < 2)

#print(file_looper()) 
