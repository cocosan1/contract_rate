import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import streamlit as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import openpyxl
from streamlit.state.session_state import Value

st.set_page_config(page_title='shop　仙台店　成約率')
st.markdown('#### shop　仙台店　成約率')

# ***ファイルアップロード 今期***
uploaded_file = st.sidebar.file_uploader('excel', type='xlsx', key='data')
df = DataFrame()
if uploaded_file:
    df = pd.read_excel(
    uploaded_file, sheet_name='受注委託移動在庫生産照会', usecols=[1, 3, 8, 16, 43, 44]) #index　ナンバー不要　index_col=0
    # 伝票番号/得意先名/商　品　名/受注日/取引先担当/お客様名
else:
    st.info('今期のファイルを選択してください。')