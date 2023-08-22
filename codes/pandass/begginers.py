import pandas as pd

double_list =[
    [1000, '과자','2019-12-31','반품'],
    [2000, '음료', '2020-03-02', '정상'],
    [3000, '아이스크림', '2020-02-03','정상'],
    [1000,'과자','2019-12-31','반품']
    ]
double_list_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(double_list, columns=double_list_columns)
# print(df_saledays)

#단일변수 처리 with apply() : 'Price' 열의 각 값에 20을 곱하여 'Sum of prices' 열을 추가
def mean_subtraction(cell_value) :
    result = 1750 - cell_value
    return result

mean_subtraction(750)

df_saledays['가격'].apply(mean_subtraction) #각 cell당 평균 차이값

# 다변수 처리  with apply()
def calculate_sum(row):
    result = row['가격'] * 20
    return result

df_saledays['가격합'] = df_saledays.apply(calculate_sum, axis='columns')
# print(df_saledays)

#regexpress(정규식) : 정규 표현식을 활용하여 이름 데이터를 추출
data = {'Names': ['김지수', '박지민', '이태용', '최수영']}

df_Name = pd.DataFrame(data)
print(df_Name)

# 정규 표현식 패턴을 정의 -> 이름에서 특정 패턴을 추출 
pattern = r'^([가-힣])'

# 'Names' 열의 값에서 정규 표현식 패턴을 추출하여 새로운 DataFrame을 생성
df_Name_extarct= df_Name['Names'].str.extract(pattern)

print(df_Name_extarct)