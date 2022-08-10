import pandas as pd 
import csv 

df = pd.read_csv('dwarf_stars.csv')
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
headers = ['Star_name', 'Distance', 'Mass', 'Radius']
##print(df.head(10))

#Converting each value under mass to a floating point
tempData_mass = []
df_mass = df['Mass']
for i in df_mass:
    i = float(i)
    revised_i = i * 0.000954588
    tempData_mass.append(revised_i)
        
##print(tempData_mass)

#Changing radius values
tempData_radius = []
df_radius = df['Radius']
for i in df_radius:
    i = i * 0.102763
    tempData_radius.append(i)

print(tempData_radius)



