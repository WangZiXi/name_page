import streamlit as st
import pandas as pd

data = pd.read_excel('积分人员对照表.xlsx')

data = data.drop_duplicates()

col1,col2 = st.columns(2)

name = col1.text_input('请输入查询的姓名')

name_in = col2.text_input('请输入录入的姓名')
page_in = col2.text_input('请输入录入的页数')
in_btn = col2.button('录入')

submit_btn = col1.button('查询')

if submit_btn:
    filtered_df = data[data['姓名'].str.contains(name)]
    col1.dataframe(filtered_df,hide_index=True)

if in_btn:
    if name_in and page_in:
        new_row = {'姓名': name_in, '页数': page_in}
        data = data.append(new_row,ignore_index=True)
        data.to_excel('积分人员对照表.xlsx',index=False)
        st.success('录入成功')
    else:
        st.warning('请输入姓名和电话')
    
