import streamlit as st
import time

st.title('streamlit 超絶な入門')

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.3)

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')

#text = st.text_input('あなたの趣味を教えてください。')
#condition = st.slider('あなたの今の調子は？',0,100,50)

#'あなたの趣味：',text,'です。'
#'コンディション：',condition,'です。'

#if st.checkbox('show image'):
#    img = Image.open('ミッドサマー.jpg')
#    st.image(img, caption='middo',use_column_width=True)