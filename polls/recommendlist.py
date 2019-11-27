import pandas as pd
import numpy as np
import sqlite3
from tqdm import tqdm


con = sqlite3.connect("C:/Users/USER/mydjango/test/django-firstweb/db.sqlite3")
cur = con.cursor()
query = cur.execute("SELECT * From polls_recommendlist")
# 칼럼명 뽑기
cols = [column[0] for column in query.description]

# 테이블을 데이터프레임으로 변환
race_result = pd.DataFrame.from_records(data=query.fetchall(), columns=cols,)
con.close()
race_result= race_result[['user_id_id','isbn_id']]

race_result['value'] = 1
matrix = race_result.pivot_table(index='user_id_id', columns='isbn_id', values='value', fill_value=0)
print(matrix.shape)

# 책의 연관성을 계산하는 식
userdf = pd.DataFrame(0, index=matrix.index, columns=matrix.index)
def pearsonR(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    return np.sum(s1_c * s2_c) / np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))
# 유사도 구하기
def Similarity(input_user, matrix, n):
    # 결과값 리스트선언
    result = []
    # 장르번호가 똑같은 책의 연관성 점수를 높이기 위해 다음 반복문을 실행
    # 0,1로 되어있는 matrix의 열(ISBN번호)을 추출해 title에 저장
    for user in matrix.index:
        # 같은 이름의 책은 연관성 비교에서 제외
        if user == input_user:
            result.append(1.00)
            continue
        # rating comparison
        # 책의 연관성을 계산
        cor = pearsonR(matrix.loc[input_user], matrix.loc[user])
        if np.isnan(cor):
            continue
        # cor 점수가 NAN 값이 아니면 result 리스트에 ISBN,cor,도서명,주제분류번호를 저장
        else:
            result.append('{:.2f}'.format(cor))
            # 후보 상위 n개만큼 리턴!
    return result[:n]
userdf

prelist = {}
def getToplisttest1(user,matrix,n):
  # 결과값 리스트선언
  booklist = []
  sumboonmo = 0
  sumboonja = 0
  a = [tuser for tuser in userdf.index if user != tuser and float(userdf.loc[user][tuser]) > 0]
  sumboonmo = sum([float(userdf.loc[user][a1]) for a1 in a ])
  for title in tqdm(matrix.columns):
       sumboonja = sum([float(userdf.loc[user][a1]) * matrix.loc[a1,title] for a1 in a ])
       if(matrix.loc[user,title]==1):
         continue
       booklist.append((title,'{:.5f}'.format(float(sumboonja/sumboonmo))))
  booklist.sort(key=lambda r: r[1], reverse=True)
  return booklist[:n]

