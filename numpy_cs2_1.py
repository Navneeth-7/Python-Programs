import pandas as pd
phy=pd.read_csv('PhysicsScoreTerm1.csv', sep=',',index_col=False)
arr=pd.DataFrame(phy)
#print(arr.describe())
arr['Name']='ALBERT YU'
print(arr.isnull().count())
#print(df)