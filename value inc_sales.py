# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 16:35:44 2025

@author: drmar
"""

import pandas as pd

#file_name=pd.read_csv('file.csv') <----- format of read_csv

data=pd.read_csv('transaction2.csv')
data=pd.read_csv('transaction2.csv',sep=';')

#summary of the data

data.info()

#playing around with variables

#working with calculations
#defining variables

CostPerItem=11.73
SellingPricePerItem=21.11
NumberofItemsPurchased=6

#mathematical operations on tableau

ProfitPerItem=21.11-11.73
ProfitPerItem=SellingPricePerItem-CostPerItem
ProfitPerTransaction=NumberofItemsPurchased*ProfitPerItem
CostPerTransaction=NumberofItemsPurchased*CostPerItem
SellingPerTransaction=NumberofItemsPurchased*SellingPricePerItem

#CostPerTransaction Column calculation
#CostPerTransaction=NumberofItemsPurchased*CostPerItem
#Variable=dataframe['Column_name']

CostPerItem=data['CostPerItem']
NumberofItemsPurchased=data['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem*NumberofItemsPurchased

#adding new column to the data frame

data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

#Sales Per transaction
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Profit=sales-cost
data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

#Markup=(sales-Cost)/Cost
data['Markup']=(data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup']=data['ProfitPerTransaction']/data['CostPerTransaction']

#rounding markup

roundmarkup=round(data['Markup'],2)
data['Markup']=round(data['Markup'],2)

#combining data fields

my_name='Dee'+'Naidoo'
my_date='Day'+'-'+'Month'+'-'+'Year'
my_data=data['Day']+'-'

#checking columns types

print(data['Day'].dtype)

#change column type

day=data['Day'].astype(str)
year=data['Year'].astype(str)
print(year.dtype)
my_date=day+'-'+data['Month']+'-'+year
data['Date']=my_date

#using iloc to view specific coulumns/rows
data.iloc[0]       #views the rows with index 0
data.iloc[0:3]     #views first 3 rows
data.iloc[-5:]     #views last 5 rows
data.head(5)       #brings first 5 rows
data.iloc[:,2]     #brings all rows and a certain column
data.iloc[4,2]     #brings certain row and a certain column

#using split to split the client keywords field
#column_var=column.str.split('sep',expand=True) <---- will split all

split_col=data['ClientKeywords'].str.split(',' ,expand=True)

#creating new coulmns for the split columns in client keywords

data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]

#using the replace function to remove the square brackets

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')

#using lower function to change words to lowercase letters
data['ItemDescription']=data['ItemDescription'].str.lower()

#joining dataset with the main data (merge files)

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files:merge_df=pd.merge(df_old,df_new,on='key')

data=pd.merge(data,seasons, on='Month')

#remove columns
#df=df.drop'columnname',axis=1(column) or 0(row)
data=data.drop('ClientKeywords', axis=1)
data=data.drop('Day', axis=1)
data=data.drop(['Month','Year'], axis=1)

#export into a csv

data.to_csv('ValueInc_cleaned.csv', index=False)































