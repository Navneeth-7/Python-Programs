import pandas as pd


df_math = pd.read_csv ('MathScoreTerm1.csv')
df_phy = pd.read_csv ('PhysicsScoreTerm1.csv')
df_dss = pd.read_csv ('DSScoreTerm1.csv')

df_math.drop(['Name', 'Ethinicity'], axis=1, inplace=True)
df_phy.drop(['Name', 'Ethinicity'], axis=1, inplace=True)
df_dss.drop(['Name', 'Ethinicity'], axis=1, inplace=True)

df_math['Score'] = df_math['Score'].fillna(0)
df_phy['Score'] = df_phy['Score'].fillna(0)
df_dss['Score'] = df_dss['Score'].fillna(0)

frames = [df_phy, df_math, df_dss]

result = pd.concat(frames)



result['Sex'] = result['Sex'].map({'M': 1, 'F': 0})
result.to_csv (r'ScoreFinal.csv')

#result.to_csv (r'ScoreFinal.csv', index = False, header=True)