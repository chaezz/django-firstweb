import pandas as pd
import sqlite3

# 이미 만든 회원,아이템들을 sqlite db에 저장하기
# 하 너무오래걸렸다 진짜 울고싶었다..
# 이유는 models.py에 만든 클래스 이름과 실제 db에 저장된 table 이름이 같은건줄 알았는데 쿼리문에서 확인해보니 둘의 이름이 달랐다.. 어쩐지 새로만들어지고 안들어가더라니..
# model은 "WebUser" 이었고 쿼리에서는 "polls_webuser" 로 저장되있었음..
# 어쨌든 이제 아래 소스들로 외부에서 만든 데이터를 저장시킬 수 있다..
# 간단하게 순서는 dataframe을 먼저 받고 sqlite의 connect로 db에 연결한다. 그리고 to_sql로 df 를 테이블에 저장시킨다. 끝나고 close로 닫기.
# 4일동안 너무 힘들었다..


# 후 몇 번 삐그덕인지 모르겠다... 이번 문제는 to_sql이다... 대여목록인 rentlist 테이블의 Foreign키인 user_id 필드가 mismatch로 오류가 뜬다..

# 같은 삽질 5일째 드디어 해결!!
# 문제는 to_sql이었다... 속성중 if_exists를 replace로 하면 table를 삭제했다가 다시 만든다.. 그렇게 되면 우리가 맨처음 만들었던 table 속성들이 전부 사라짐..ex)pk설정
# admin에 보이기는 하지만 외래키로 값을 불러올 수 없었다...그리고 pk가 아니니 중복될 수 있음..
# 해결방법은 if_exists를 append로 바꾸는것이다. 그렇게 되면 기존테이블을 삭제안하고 컬럼명에 맞게 들어간다.
# 추가로 to_sql할 경우 index컬럼이 자동으로 들어가는데 기존 테이블에는 index가 없으니 false를 선언해준다.

# df = pd.read_csv("usertable500.csv", encoding='cp949')
# con = sqlite3.connect("C:/Users/USER/mydjango/test/django-firstweb/db.sqlite3")
# df.to_sql('polls_webuser',con, if_exists='append',index=False)
# con.close()

# df = pd.read_csv("itemtable500.csv", encoding='cp949')
# con = sqlite3.connect("C:/Users/USER/mydjango/test/django-firstweb/db.sqlite3")
# df.to_sql('polls_book',con, if_exists='append',index=False)
# con.close()

# ??? 갑자기 컬럼명 혼돈이 왔다..
# 분명히 user_id라고 생성했지만 생겨난 컬럼명은 user_id_id네 왜이러지..ㅎㅎ;;;
# 암튼 꾸역꾸역 넣기 성공!
# 인줄알았으나 user_id가 안들어가짐... 소숫점있어서 그런듯..
# int형으로 바꾸니까 해결!
df = pd.read_pickle("500x500rentlist(수정).pkl")
df = df.rename(columns={'회원번호':'user_id_id','ISBN':'isbn_id'})
df['date'] = 1
df['user_id_id'] = df['user_id_id'].astype('int')
print(df.head())
con = sqlite3.connect("C:/Users/USER/mydjango/test/django-firstweb/db.sqlite3")
df.to_sql('polls_rentlist1',con, if_exists='append',index=False)
con.close()
