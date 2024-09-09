import streamlit as st

view = [100, 150, 30]
st.write('# Youtube view')
st.write('## raw')
view

st.write('## bar chart')
st.bar_chart(view)


# 데이터 사이언스에서 가장 많이 사용하는 pandas, numpy -> streamlit이 이것을 인식함
import pandas as pd
sview = pd.Series(view)     # Pandas 데이터 타입으로 넣는 코드 (컨버팅)
sview



# 웹으로 deploy 하기 위한 절차
# 1. git에 올려야 함
# 2. github.com으로 보내야 함
# 3. streamlit cloud가 땡겨옴