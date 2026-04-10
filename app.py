import streamlit as st

st.title('나의 첫 웹서비스 만들기!!!')
name = st.text_input('이름을 입력하세요: ')
game = st.selectbox('좋아하는 음식을 선택하세요: ', ['롤','발로란트'])
if st.button('인사말 생성') : 
  st.write(f'{name}님! 당신이 좋아하는 음식은 {game}군요!')
                    
             
