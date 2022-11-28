import pandas as pd
import math

EXPECTED_PERCENTAGE = {
    "1": 0.301, 
    "2": 0.176,  
    "3": 0.125, 
    "4": 0.097, 
    "5": 0.079, 
    "6": 0.067, 
    "7": 0.058, 
    "8": 0.051, 
    "9": 0.046
}


original_data=pd.read_csv("test.csv")
#data=pd.read_csv('test.csv')

#Taking 'Volume' column for testing benford law
data=original_data['data']


#Storing 1st digits of all volume value
leading_digit_list=[]
for i in list(data):
    leading_digit_list.append(str(i)[0])


#Checking unique value in the list
set(leading_digit_list)


#As first digit cannot be '0', Removing
while '0' in leading_digit_list:
    leading_digit_list.remove('0')
leading_digit_list.sort()


total_digits = len(leading_digit_list)
print("Total Instances in the dataset is",total_digits)


expected_frequency = {}
for num in EXPECTED_PERCENTAGE:
    expected_frequency[num] = EXPECTED_PERCENTAGE[num] * total_digits

#Calculating the frequency of each digit occured
observed_frequency={}
for i in leading_digit_list:
    if i in observed_frequency.keys():
        observed_frequency[i]+=1
    else:
        observed_frequency[i]=1


#Normalizing
frequency = {}
for i in observed_frequency:
   frequency[i] = observed_frequency[i]/total_digits*100

#chi square test
chi_square_sum = 0
for i in range(1, 10):
    chi_square = math.pow(observed_frequency[str(i)] - expected_frequency[str(i)], 2)
    chi_square_sum += chi_square/expected_frequency[str(i)]

f = None
if chi_square_sum < 15.51:
    f = frequency
else:
    f="Donot follow Benford Law"

