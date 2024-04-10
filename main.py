import streamlit as st
import pandas as pd
import requests
import io
import base64


def save_to_github(username, repo_name, file_path, file_content, token):
    url = f'https://api.github.com/repos/{username}/{repo_name}/contents/{file_path}'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'message': 'Update Excel file',
        'content': base64.b64encode(file_content).decode('utf-8')  # 将字节流转换为 Base64 编码的字符串
    }
    response = requests.put(url, headers=headers, json=data)
    return response.status_code == 200

username = 'WangZiXi'
repo_name = 'name_page'
file_path = '积分人员对照表.xlsx'
token = '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'

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
        new_row = pd.DataFrame({'姓名':[name_in],'页数':[page_in]})
        data = pd.concat([data,new_row],ignore_index=True)
         # 创建一个字节流
        excel_buffer = io.BytesIO()
        # 将数据写入字节流中
        data.to_excel(excel_buffer, index=False)
        # 重置字节流的指针位置
        excel_buffer.seek(0)
        excel_data = excel_buffer.getvalue()
        # excel_data = data.to_excel(None,index=False)
        if save_to_github(username,repo_name,file_path,excel_data,token):
            st.success('录入成功')
        else:
            st.error('录入失败')
    else:
        st.warning('请输入姓名和电话')
    
    
