<details open>
<summary>TitanicFromDisaster</summary>

#### DDA

| Variable | Definition | Key | 분석가의견
| --- | --- | --- | ---- |
| PassengerId |  |  | 필요없음 데이터 분석 x |
| survival | Survival | 0 = No, 1 = Yes | 범주형(명목형), 확인 결과 데이터 타입이 결정됨. |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형(순서형),확인 결과 데이터 타입이 결정됨. |
| sex | Sex |male  /  female | 범주형 , male/female 의 범주로 나뉨. |
| Age | Age in years | | 수치형(이산형): 연령 or 범주형(순서형) : 연령대별,세분화 분석 일때 |
| sibsp | # of siblings / spouses aboard the Titanic | |수치형, 사람들의 형제자매나 배우자의 수 구분한 정보|
| parch | # of parents / children aboard the Titanic | |수치형 ,  탑승한 부모 또는 자녀의 수를 구분한 정보|
| ticket | Ticket number | |범주형(명목형), 숫자로 표현되지만 티켓 가격같이 내용을 나타내는 숫자가 아니라 티켓별 고유번호로 다른 티켓들을 구분함|
| fare | Passenger fare | | 수치형, 티켓가격은 여러 가지 금액을 나타내는 수치값 |
| cabin | Cabin number | |범주형(명목형), 객실 번호나 위치를 나타내기 위해 구분함 특정한 순서나 계층구조를 갖지 않음 |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 범주형,각각 승선한 항구를 나타내는 범주적인 정보|

</details>



<details open>
<summary>TypeOfContractChannel</summary>

#### DDA
| Variable | Definition | Key | analyst opinion
| --- | --- | --- | ---- |
| id |unique id | | | 필요없음 데이터 분석 x
| type_of_contract | contract type | 렌탈, 멤버십 , NaN | 범주형(명목형) 계약 유형 나타냄| 
| type_of_contract2| Additional Contract Types | 'Normal', 'Extension_Rental', 'TAS', 'Promotion', 'Package', nan,'TA1', 'TA3', 'Group', 'TA2' | 범주형(명목형) 추가 계약 유형별 나타냄  |
| channel | Communication channels | '서비스 방문', '홈쇼핑/방송', '렌탈재계약', '렌탈총판', '전자랜드', '홈플러스', '일반', '영업방판','하이마트', '이마트', '홈쇼핑/인터넷', 'R빌리미', 'R유통사', 'R인터넷', 'R관리방판','R농협인터넷몰', 'R농협', 'R법인', 'R렌탈운영', 'R법인그룹'| 범주형(명목형) 커뮤니케이션 채널들 별 상태를 나타냄 |
| datetime | timestamp of the incident | | 수치형(연속형),평상시 모든 날짜 숫자화 가능|
| Term | term or term of the contract | | 범주형(명목형) , 숫자로 표현되지만 각 값들은 계약 기간이나 기간으로 나타나 순서가 없는 명목형 타입  |
| payment_type | payment method |'CMS', '카드이체', '가상계좌', '지로', '무통장' | 범주형(명목형), 서로 각각 다른 타입의 지불방법임|
| product | product or service |'K1', 'K3', 'K2', 'K4', 'K6', nan, 'K5' | 범주형(명목형) , 각각의 자동차 고유 이름이고 표현된 숫자는 버전을 식별하는 값이라 순서와 상관없음 |
| amount | Amount | | 수치형(이산형),특정한 금액을 나타내는 구체적인 숫자 값이고 연속적인 값이 없음  |
| state | 현재 계약 상태 | '계약확정', '해약확정', '기간만료', '해약진행중' | 범주형(명목형) , 계약과 관련된 다양한 상태나 상황 나타냄 |
| overdue_count | Number of Overdue Payments | | 수치형(이산형) , 연체 수를 나타내는 숫자 값이고 연속적인 값이 아님| 
| overdue | delinquent status | '없음', '있음', nan | 범주형(명목형)  |
| credit rating | Credit Score or Rating | | 수치형(이산형),특정한 이자율을 나타내는 숫자 값이고 연속적인 값이 아님 |
| bank | bank or financial institution | 은행종류들 | 범주형(명목형), 서로 각각 다른 은행임|
| cancellation | Termination Status |'정상', '해약', nan | 범주형(명목형) |
| age | individual age | | 수치형(이산형): 연령 or 범주형(순서형) : 연령대별,세분화 분석 일때 |
| Mileages | mileage or usage data | | 수치형(이산형),특정한 마일리지값을 나타내는 숫자 값이고 연속적인 값이 아님 |
</details>


