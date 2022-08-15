import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

#どちらでも表を表示させれれる
# st.write(df)
# st.dataframe(df, width=100, height=100) #表示サイズ指定可能
st.dataframe(df.style.highlight_max(axis=0)) #最大値をハイライト

# st.table(df) #静的なテーブル


#マークダウン
"""
# タイトル
## サブタイトル
### 内容

"""

#コード表示
code = '''def hello():
     print("Hello, Streamlit!")'''

st.code(code, language='python')


#折れ線グラフ
df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

text = st.sidebar.text_input('あなたの趣味は？')
'あなたの趣味：',text