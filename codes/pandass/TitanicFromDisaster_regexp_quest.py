# Quest
# - Name 변수에서 성씨만 가져오기
# - hint : 결혼유무 컬럼에 Nan 없어야 함
# 결혼유무 : apply()
# 성씨 : extract() 

import pandas as pd

df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
# print(df_TFD)

df_extarct = df_TFD['Name']
df_extarct = pd.DataFrame(df_extarct)
# print(df_extarct)


# 성씨 패턴정의 :  ^ 문자열시작 , [A-Za-z] 대문자 소문자 모든 문자 , + 계속연속발생
pattern = r'^([A-Za-z]+)'   

# 특정 패턴을 추출 : 'Name' 열의 값에서 정규 표현식 패턴을 추출하여 새로운 DataFrame을 생성
df_extarct['Last_Name']= df_extarct['Name'].str.extract(pattern)
# print(df_extarct['Last_Name'])


#결혼유무 함수
def extract_status(name):
    if 'Mrs.' in name:
        return '기혼'
    elif 'Mr.' in name:
        return '미혼 (남성)'
    elif 'Miss.' in name:
        return '미혼 (여성)'
# pattern_married = r'(?:Mrs\.|Mr\.|Miss\.)'   


df_extarct['Status'] = df_TFD['Name'].apply(extract_status)
df_extarct=df_extarct.dropna()    #결혼유무 컬럼에 Nan 없애기 

print(df_extarct[['Name','Last_Name','Status']])