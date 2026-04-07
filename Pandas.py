import pandas as pd
 data1={
"Name": ['riya', 'jiya', 'liza'], 
 "Roll": ['12', '23', '21'],
"Marks": ['20', '12', '19']
}
df1=pd.DataFrame(data1)
data2={
"Name": ['riya', 'jiya', 'liza'],
 "Roll": ['12', '23', '21'],
"Attendance": ['70%', '80%',  '90%']
}
df2=pd.DataFrame(data2) 
df3=pd.merge(df1,df2.on='Roll',how='outer')
 print(df3)
