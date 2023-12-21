##  ✅ Gathering Datas

### ✔ Python Selenium 웹 스크래핑
-  Selenium : 동적 웹 페이지에서 데이터를 수집하기 위해서 사용하는 자동화 라이브러리 
- 웹 스크래핑(Web scraping) vs 웹 크롤링(Web Crowling) 차이점
  - 참고 : https://blog.naver.com/hectodata/222721006534
- 웹 크롤링을 배운 이유는 더 많은 데이터를 활용하여 데이터 분석을 더 효과적으로 수행하기 위해서입니다. 이번 수업을 통해 방대한 데이터를 가져오는 방법을 알게 되었고 이렇게 많은 데이터를 활용하여 분석을 하면 더 정확한 분석이 나올거라고 생각이 듭니다.

| 분류 | 주요 내용 | 작성코드 | 
| -- | -- | -- | 
| browser | 브라우저 창 띄우기  | [begginer](./codes/gatheringdatas/seleniums/begginer.ipynb) | 
| 이미지저장 | 홈페이지 스크린샷 이미지 저장하기| [image](./codes/gatheringdatas/seleniums/begginers.ipynb) | -- |
| element | 이마트몰에서 element 가져오기 , 묶음에서 list 만들기 | [EmartMall](./codes/gatheringdatas/seleniums/emartmall_find.ipynb)  | -- |
| paginations | 이마트몰안에 페이지네이션 |  [paginations](./codes/gatheringdatas/seleniums/emartmall_paginations.ipynb)  | -- |
|login| 깃허브 로그인하기 |[github_login](./codes/gatheringdatas/seleniums/github_events.ipynb) | -- |
|login| 잡플래닛 로그인하기 |[jobplanet_login](./codes/gatheringdatas/seleniums/jobplanet_login.ipynb) | -- |
|single| googlestore 에서 healthcare앱 하나 선택해 클릭후 정보 가져오기(서비스명, 만든회사,앱정보), 리뷰가져오기(내용,날짜,별점),추가댓글,클릭갯수 가져오기 |[healthcare_single](./codes/gatheringdatas/seleniums/googlestore_healthcare_single.ipynb) | -- |
|loops| googlestore 에서 healthcare 부분에 있는 모든 앱  정보 가져오기(서비스명, 만든회사,앱정보), 전체 리뷰가져오기(내용,날짜,별점) -for문사용  |[healthcare_loops](./codes/gatheringdatas/seleniums/googlestore_healthcare_loops.ipynb) | -- |
|loops_complete| googlestore 에서 healthcare 최종 |[heathcare_loops_complete](./codes/gatheringdatas/seleniums/googlestore_heathcare_loops_complete.ipynb) | -- |

 
### ✔ MongoDB
 MongoDB란 : 
- NoSQL 데이터베이스 중 하나로, 특히 문서 지향적(Document-Oriented) 데이터베이스
-  데이터는 BSON(Binary JSON) 형태로 저장
-  확장성
-  대량의 데이터를 처리하고 저장할 수 있으며, 데이터의 분산 처리가 가능하기 때문에 많은 양의 데이터를 효율적으로 관리 가능

| 분류 | 주요 내용 | 작성코드 | 
| -- | -- | -- | 
| findwithpandas | 브라우저 창 띄우기  | [findwithpandas](./codes/gatheringdatas//mongodb/findwithpandas.ipynb) |

- 5천개 이상의 데이터를 하나씩 for문을 돌려서 새로운 db를 row에 추가하는 것은 무리가 가는 코드이므로 mongodb를 사용하여 한번에 추가해 새로운 디비를 완성하는게 더 효율적이기 때문에 사용함
  


## ✅ NLP (자연어 처리)
 - 검색 엔진, 기계 번역, 감성 분석 등 다양한 분야에서 활용하기 위하여 자연어 처리를 함 

## ✅ Pandas
- 대량의 데이터를 효율적으로 처리하고 가공
-  CSV, 텍스트, Excel, SQL 데이터베이스 등 다양한 형태의 데이터를 쉽게 분석 가능
  
## ✅ Visuallizations
- 시각화 :  파이썬에서 Matplotlib, Seaborn, Plotly 등의 라이브러리를 사용하여 다양한 시각화 생성
  
| 분류 | 주요 내용 | 작성코드 | 
| -- | -- | -- | 
| 시각화  |   | [findwithpandas(./codes/gatheringdatas//mongodb/findwithpandas.ipynb)] |

## ✅ DDA
### ✔ Descriptive Data Analysis  
- 묘사적 데이터 분석
- 수집된 데이터를 이해하고 요약하는 과정으로 데이터의 현재 상태를 정확하게 파악하고, 데이터의 중심 경향, 분포, 분산 등을 확인하는데 사용
- 주요 사용되는 통계량 :  평균, 중앙값, 최빈값, 범위, 분산, 표준편차, 백분위수 등
  
| 분류  | 작성코드 | 
| -- | -- | 
| DDA 선결 | [mixed_Normal](codes/DDA/RecurrenceOfSurgery_DDA_quests.ipynb) |

## ✅ EDA
### ✔ Exploratory Data Analysis 
- 탐색적 데이터 분석
- 수데이터의 패턴, 이상치, 변수 간의 관계 등을 파악하여 분석 방향 설정하는 중요한 역할
- 가능성이 큰 X-Y 관계 가설 도출
- Matplotlib, Seaborn 등의 라이브러리를 활용

## ✅ CDA
### ✔Confirmatory Data Analysis
- 확증적 데이터 분석
- 미리 설정된 가설이나 이론을 데이터를 통해 검증하는 분석 방법
- p-value 기준 의사결정

| 분류  | 작성코드 | 
| -- | -- | 
| categories CDA  | [categories](codes/CDA/TypeOfContractChannel_CDA_categories.ipynb) | 
| continuous CDA  | [continuous](codes/CDA/TypeOfContractChannel_CDA_continuous_quest.ipynb) | 
| mixed_Normal CDA  | [mixed_Normal](codes/CDA/TypeOfContractChannel_CDA_mixed_Normal.ipynb) | 
| mixed_unNormal CDA  | [mixed_unNormal](codes/CDA/TypeOfContractChannel_CDA_mixed_unNormal.ipynb) | 
| singlevalue CDA  | [singlevalue](codes/CDA/TypeOfContractChannel_CDA_singlevalue.ipynb) | 


## 📑 Quest 
| 분류 | 주요 내용 | 작성 코드 | 
| -- | -- | -- | 
|Selenium | 도서목록 제목만 스크래핑해서 csv로 저장하기 | [ brunch_books_title](./codes/gatheringdatas/seleniums/brunch_books_title_quest.ipynb.ipynb)  | 
|Selenium| 네이버 로그인하기 로그인 후 메일로 이동하기 |[naver_login](./codes/gatheringdatas/seleniums/naver_login_quest.ipynb) |
|Selenium| 코리안즈의 게시물 번호, 제목, 게시날짜, 조회수, 상세 채널 리스트(채널명, 링크) 가져오기 , 범위 : 1page ~ 10page |[koreanz_xyz](./codes/gatheringdatas/seleniums/koreanz_xyz_quest.ipynb.ipynb) |
|NLP| 머신러닝 이용 감성 분석,영화 댓글 학습 ( 0:부정, 1:긍정 ) |[navermovierating_mechinelearning](./codes/gatheringdatas/NLP/navermovierating_mechinelearning_quest.ipynb) |


### 📚 사용기술
<div>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">
<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> 
<img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>
