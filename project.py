import warnings; warnings.simplefilter('ignore')
import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from scipy.stats.stats import pearsonr

data = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
B, K = data.shape
print(f'baris : {B}, kolom : {K}')
print(data.head(10))

for i in ['Platform', 'Genre', 'Publisher', 'Developer']:
    data[i] = data[i].astype('category')

# Mengubah type data Stars dari object menjadi numerik(float64)
data['User_Score'] = pd.to_numeric(data['User_Score'], errors='coerce')

#menghilangkan missing value dengan mean
data['Critic_Score'].fillna(data['Critic_Score'].mean(), inplace=True)
data['Critic_Count'].fillna(data['Critic_Count'].mean(), inplace=True)
data['User_Score'].fillna(data['User_Score'].mean(), inplace=True)
data['User_Count'].fillna(data['User_Count'].mean(), inplace=True)
# Trimming : IQR
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
print(IQR) # Menghitung jumlah data setelah di trim dengan IQR

print(data.describe(include='all'))

plt.figure(figsize=(9,7))
sns.countplot(data=data, y='Platform', palette='Set2')
plt.show()
