import pandas as pd
import folium



#pop_data = xls
#cctv_data = csv
#print(aa.head())
#print(xls.head())

ctx='../data/'
xls = pd.read_excel(ctx+ 'population_in_Seoul.xls'
                    ,encoding='UTF-8'
                    ,header=2
                    ,usecols='B,D,G,J,N')
csv = pd.read_csv(ctx +'CCTV_in_Seoul.csv')

pop_data = xls
cctv_data = csv

cctv_data_schema = cctv_data.columns
pop_data_schema = pop_data.columns

""""""
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

'자치구', '계', '계.1', '계.2', '65세이상고령자', '65세이상고령자'
""""""

cctv_data.rename(columns={cctv_data.columns[0]:'구별'},inplace=True)
# inplace=True 실제 변수의 내용을 바꿔라

pop_data.rename(columns={pop_data.columns[0]:'구별'
                         ,pop_data.columns[1]:'인구수'
                         ,pop_data.columns[2]:'한국인'
                         ,pop_data.columns[3]:'외국인'
                         ,pop_data.columns[4]:'고령자'}
                    ,inplace=True)
print(pop_data.columns)