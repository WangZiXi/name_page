import streamlit as st
import pandas as pd
import requests
from github import Github
import os


username = 'WangZiXi'
password = os.getenv('key')
repo_owner = 'WangZiXi'
repo_name = 'name_page'
file_path = 'users.txt'

g = Github(username,password)

repo = g.get_user(repo_owner).get_repo(repo_name)

def save_to_github(data):
    contents = repo.get_contents(file_path)
    existing_data = contents.decoded_content.decode('utf-8')
    updated_data = existing_data + '\n' + data

    repo.update_file(file_path, "Update user data", updated_data,contents.sha)

    st.success('录入成功')

contents = repo.get_contents(file_path)
data = contents.decoded_content.decode('utf-8')

col1,col2 = st.columns(2)

name = col1.text_input('请输入查询的姓名')

name_in = col2.text_input('请输入录入的姓名')
page_in = col2.text_input('请输入录入的页数')
in_btn = col2.button('录入')

submit_btn = col1.button('查询')

if submit_btn:
    for line in data:
        st.write(line)
        # 去除行末尾的换行符
        line = line.strip()
        # 检查该行是否包含姓名为王新
        if name in line:
            # 输出满足条件的行
            st.code(line,language='text')
    

if in_btn:
    if name_in and page_in:
        user_data = f'姓名：{name_in},页数：{page_in}'
        save_to_github(user_data)
    else:
        st.warning('请输入姓名和页数')
    
    
