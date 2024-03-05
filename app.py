import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime as dt
import datetime
accept_multiple_files=True

st.title('포트폴리오 기록장, 좋아해')
st.subheader('# 좋은점, 아쉬운 점, 해볼만한 점 ')

def main():
    st.subheader("#너의 포트폴리오를 보여줘")
    upload_files = st.file_uploader("여러 사진을 업로드 해주십쇼",accept_multiple_files=True)

    if upload_files:
        image_files = list(upload_files)
        image_files.sort(key= lambda x: x.name)

        st.write(f"총 {len(image_files)}개의 사진이 업로드 되었습니다~")

        index = st.slider("이미지 선택 ", 0, len(image_files)-1, 0)
        st.image(image_files[index], use_column_width=True, caption=image_files[index].name)

if __name__ == '__main__':
    main()

my_date = st.date_input("날짜 입력")
st.text(my_date)

def main() :
    
    my_time = st.time_input('시간 선택')
    st.write(my_time)
  
if __name__ == "__main__" :
    main()

def main() :

    language = ['영어', '수학', '코딩', '국어', '과학','디자인','게임','자바','c언어','PHP','파이썬']
    st.multiselect('너의 포트폴리오를 나타내는 키워드는? (복수 선택 가능)', language)

if __name__ == "__main__" :
    main()

# main()
def main() :

    language = ['영어', '수학', '코딩', '국어', '과학','디자인','게임','기타']
    my_choice = st.selectbox('어떤 걸 위주로 공부했니?', language)

    if my_choice == language[0] :
        st.write('영어를 선택하셨습니다.')
    elif my_choice == language[1] :
        st.write('수학을 선택하셨습니다.')
    elif my_choice == language[2] :
        st.write('코딩을 선택하셨습니다')
    elif my_choice == language[3] :
        st.write('국어를 선택하셨습니다')
    elif my_choice == language[4] :
        st.write('과학을 선택하셨습니다')       
    elif my_choice == language[5] :
        st.write('디자인을 선택하셨습니다')   
    elif my_choice == language[6] :
        st.write('게임을 선택하셨습니다')       
    elif my_choice == language[7] :
        st.write('기타를 선택하셨습니다')       
      



if __name__ == "__main__" :
    main()

memo = st.text_area('기록하기', height = 200)
save_button = st.button('저장~')

if save_button: 
    with open('memo.txt', 'w', encoding = "UTF-8") as file : 
        file.write(memo)
        st.success('메모가 저장되었습니다~')


#저장된 메모 확인
st.subheader('저장된 기록')
try: 
    with open('memo.txt', 'r', encoding="UTF-8") as file: 
        saved_memo = file.read()
        st.write(saved_memo)
except FileNotFoundError:
    st.info('저장된 메모가 없습니다~')
       