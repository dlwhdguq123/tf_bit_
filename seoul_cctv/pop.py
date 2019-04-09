import pandas as pd
import folium



#pop_data = xls
#cctv_data = csv
#print(aa.head())
#print(xls.head())

ctx='../data/'
pop_data= ctx+ 'population_in_Seoul.xls'
cctv_data = ctx +'CCTV_in_Seoul.csv'
aa = pd.read_excel(pop_data)
xls = pd.read_csv(cctv_data)

print(aa.head())
print(xls.head())

