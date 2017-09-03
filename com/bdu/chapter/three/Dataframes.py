import datetime
import pandas as pd
import numpy as np


todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

columns = ['A','B', 'C']

print(columns)

df_ = pd.DataFrame(index=index, columns=columns)

print (df_)
df_ = df_.fillna(0) # with 0s rather than NaNs

print (df_)

data = np.array([np.arange(10)]*3).T

print (data)

df = pd.DataFrame(data, index=index, columns=columns)

print (df)
print ("all column heading")
print (df[0:0])

print ("access specific row")
print (df[1:2])

print (df[:2])

print (df[2:])

print (df['A'])

print (sum(df['A']))

print (df.tail(4)) #default is 5


print (df.head(4))#default is 5

addData = {'A':[2,6,0],'B':[4,6,3],'C':[1,5,4]}

df = pd.DataFrame(addData)

print (df)

df['genre'] = 'pop','rock','hard rock'

print (df)

print ("inserting a new row")

df.append( {'A':5,'B':4,'C':6,'genre':'added'},ignore_index=True)

print(df)

df.drop(2)

df.drop('genre',1)

print (df)