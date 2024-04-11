import streamlit as st
import pandas as pd
import requests
from github import Github


username = 'WangZiXi'
password = 'wangxin083'
repo_owner = 'WangZixi'
repo_name = 'name_page'
file_path = 'name_page/users.txt'
# token = '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'

g = Github(username,password)

repo = g.get_user(repo_owner).get_repo(repo_name)

def save_to_github(data):
    contents = repo.get_contents(file_path)
    existing_data = contents.decoded_content.decode('utf-8')
    updated_data = existing_data + '\n' + data

    repo.update_file(file_path, "Update user data", updated_data,contents.sha)

    st.success('录入成功')

# data = pd.read

contents = repo.get_contents(file_path)
data = contents.decoded_content.decode('utf-8')
st.code(data, language='text')

# data = data.drop_duplicates()

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
        # new_row = pd.DataFrame({'姓名':[name_in],'页数':[page_in]})
        # data = pd.concat([data,new_row],ignore_index=True)
        # excel_data = data.to_excel(file_path,index=False)
        # if save_to_github(username,repo_name,file_path,excel_data,token):
        #     st.success('录入成功')
        # else:
        #     st.error('录入失败')
        user_data = f'姓名：{name_in},年龄：{page_in}'
        save_to_github(user_data)
    else:
        st.warning('请输入姓名和电话')
    
    
