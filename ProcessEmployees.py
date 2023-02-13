'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
EMPFILE = 'employee_data.csv'

infile = open(EMPFILE, 'r', newline= '')

reader = csv.reader(infile)
next(reader)
#create an empty dictionary
new_dict = {}

#use a loop to iterate through the csv file
for row in reader:
  f_name = row[1]  
  l_name = row[2]
  department = row[3]
  title = row[4]
  salary = float(row[5])

  salary_calc = salary * 0.1
  new_salary = salary_calc + salary 

  #check if the employee fits the search criteria
  if department == 'Marketing':
    if title == 'CSR':
        print('Manager Name:', f_name, l_name, 'Current Salary:','$' + format(salary, ',.2f'))

        
        

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
new_dict ={f_name: {l_name: new_salary}}

for dict in new_dict:
   print('Manager Name:', dict, 'New Salary:', dict[l_name])


          
        

        
infile.close() 
