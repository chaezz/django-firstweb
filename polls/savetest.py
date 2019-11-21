import pandas as pd
import sqlite3

# 이미 만든 회원,아이템들을 sqlite db에 저장하기
# 하 너무오래걸렸다 진짜 울고싶었다..
# 이유는 models.py에 만든 클래스 이름과 실제 db에 저장된 table 이름이 같은건줄 알았는데 쿼리문에서 확인해보니 둘의 이름이 달랐다.. 어쩐지 새로만들어지고 안들어가더라니..
# model은 "WebUser" 이었고 쿼리에서는 "polls_webuser" 로 저장되있었음..
# 어쨌든 이제 아래 소스들로 외부에서 만든 데이터를 저장시킬 수 있다..
# 간단하게 순서는 dataframe을 먼저 받고 sqlite의 connect로 db에 연결한다. 그리고 to_sql로 df 를 테이블에 저장시킨다. 끝나고 close로 닫기.
# 4일동안 너무 힘들었다..



# df = pd.read_csv("usertable500.csv", encoding='cp949')
# con = sqlite3.connect("C:/Users/USER/mydjango/django-firstweb/db.sqlite3")
# df.to_sql('polls_webuser',con, if_exists='replace')
# con.close()

# df = pd.read_csv("itemtable500.csv", encoding='cp949')
# con = sqlite3.connect("C:/Users/USER/mydjango/django-firstweb/db.sqlite3")
# df.to_sql('polls_book',con, if_exists='replace')
# con.close()


df = pd.read_pickle("500x500rentlist(수정).pkl")
con = sqlite3.connect("C:/Users/USER/mydjango/django-firstweb/db.sqlite3")
df.to_sql('polls_rentlist',con, if_exists='replace')
con.close()
