# sample to clear the place

import streamlit as st
import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from main import User, engine, SessionLocal
from pydantic import BaseModel
from typing import List
import json
import pandas as pd
import numpy as np
import datetime as dt
# from datetime import datetime, timedelta New name

API_URL_users = "http://localhost:8000/users/"
API_URL_links = "http://localhost:8000/links/"
API_URL_meetings = "http://localhost:8000/meetings/"
API_URL_projects = "http://localhost:8000/projects/"

def main():
    # initilization
    # ------------------------------------------
    dict_user = {'name' : ['Michiba', 'Tanaka', 'Suzuki'],
            'mail_add' : ['A', 'B', 'C'],
            'pw' : ['1', '2', '3']
    }
    
    dict_user_R = {'name': ['Michiba'],
                   'mail_add': ['A'],
                   'pw': ['1']}
    
    dict_display = {'name': ['sub_log', 'sub_select_item_and_CRUD', 
                             'main_link_C', 'main_link_R','main_link_U','main_link_D',
                             'main_meeting_C', 'main_meeting_R','main_meeting_U','main_meeting_D',
                             'main_project_C', 'main_project_R','main_project_U','main_project_D'],
                    'status': [True, False, False, False, False, False, False, False, False, False, False, False, False, False]
    }
    dict_link = {'name': ['Apple', 'orange'],
                 'url': ['https://apple.com', 'B'],
                 'category': ['a', 'c'],
                 'status': ['a', 'b'],
                #  'mail_add': ['a', 'b'],
                 'id_user': ['1', '2'],
                 }
    dict_meeting = {'name': ['a'],
                    'description': ['b'],
                    'category': ['Private'],
                    'status': ['Open'],
                    'start_datetime': ['2024-02-14T01:00:00'],
                    'end_datetime': ['2024-02-14T12:00:00'],
                    'id_user': ['1']
                    }
    
    dict_project = {'name': ['a'],
                    'country': ['Malaysia'],
                    'client': ['NEC'],
                    'type_of_building': ['Factory'],
                    'total_floor_area': ['10000.0'],
                    'm_amount': ['1000000'],
                    'currency': ['RM'],
                    'date_of_submission': ['2024-02-14'],
                    'id_user': ['1']
                    }
    
    dict_time_zone = {'city': ['SIN/KL/MNL/BJN/TPI', 'BKK/JKT/HNI', 'TKY', 'NDL', 'LDN'],
                      'time': [8, 7, 9, 5.5, 0],
                     }      
    # list for link and meeting
    category_list = ['Private', 'Public', 'Company', 'test']
    status_list = ['Open', 'Public', 'Private', 'Secret', 'test']
    
    
    
    # project for link
    country_list = ['Singapore', 'Malaysia', 'Indonesia', 'Thai', 'Philippines', 'China', 'Hong Kong', 'Taiwan', 'India', 'Bangladesh']
    currency_list = ['USD', 'JPY', 'SGD', 'RM', 'IRP']
    type_of_building_list = ['Factory', 'Warehouse', 'Office', 'Data_center']

    
    
    
    if 'log_in_mail' not in st.session_state:
        st.session_state['log_in_mail'] = 'ok'
        
    if 'log_in_id' not in st.session_state:
        st.session_state['log_in_id'] = None
        
    df_time_zone = pd.DataFrame(dict_time_zone)  
    if 'time_zone' not in st.session_state:
        st.session_state['time_zone'] = df_time_zone
        
    df_display = pd.DataFrame(dict_display)
    if 'display_data' not in st.session_state:
        st.session_state['display_data'] = df_display
        
    df_user = pd.DataFrame(dict_user)
    df_user_R = pd.DataFrame(dict_user_R)
    if 'user_data' not in st.session_state:
        # st.session_state['user_data'] = df_user
        st.session_state['user_data'] = df_user_R
        for i in(range(int(len(dict_user['name'])))):
        
            data_a = {'name': dict_user['name'][i],
                    'mail_add': dict_user['mail_add'][i],
                    'pw': dict_user['pw'][i]
                    }
        
            response = requests.post(API_URL_users, json.dumps(data_a))

    
        
    df_link = pd.DataFrame(dict_link)    
    if 'link_data' not in st.session_state:
        # st.write('link')
        st.session_state['link_data'] = df_link

            
        data = {'name': 'a',
                'url': 'a',
                'category': 'a',
                'status': 'a',
                'id_user': 'a',
                }
            
        
    df_meeting = pd.DataFrame(dict_meeting)  
    if 'meeting_data' not in st.session_state:
        
        st.session_state['meeting_data'] = df_meeting
        
        data_meeting = {'name': 'a',
                'description': 'a',
                'category': 'a',
                'status': 'a',
                'start_datetime': '2024-02-14T01:00:00',
                'end_datetime': '2024-02-14T12:00:00',
                'id_user': '1',
                }
        
            # st.wriponse.status_code)
        
    df_project = pd.DataFrame(dict_project)  
    if 'project_data' not in st.session_state:
        
        st.session_state['project_data'] = df_project
        
        data_project = {'name': 'a',
                    'country': 'Malaysia',
                    'client': 'NEC',
                    'type_of_building': 'Factory',
                    'total_floor_area': '10000.0',
                    'm_amount': '1000000',
                    'currency': 'RM',
                    'date_of_submission': '2024-02-14',
                    'id_user': '1'
                    }
        # response = requests.pe : {response.status_code}")
        
        


    # control display
    # ------------------------------------------ table
    
    time_zone_list = st.session_state['time_zone']['city']
    time_zone_select = st.sidebar.selectbox('time_zone', time_zone_list)
    
    if get_status_by_name('sub_log'):
        
        sub_log(df_display, df_user)
    else:
        pass
        
    if get_status_by_name('sub_select_item_and_CRUD'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        sub_select_item_and_CRUD(df_display, df_user)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    # handle link
    # ----------
    
    if get_status_by_name('main_link_C'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_link_C(category_list, status_list)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_link_R'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_link_R()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_link_U'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_link_U(category_list, status_list)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_link_D'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_link_D()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    # handle meeting
    # ----------
    
    if get_status_by_name('main_meeting_C'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_meeting_C(time_zone_select)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_meeting_R'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        # st.write('main_meeting_R')
        # main_meeting_C(time_zone_select)
        main_meeting_R(time_zone_select)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_meeting_U'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_meeting_U(time_zone_select)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_meeting_D'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_meeting_D()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    # -----------
    
    if get_status_by_name('main_project_C'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_project_C()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_project_R'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        # st.write('main_project_R')
        # main_project_C(time_zone_select)
        main_project_R(time_zone_select)
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_project_U'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        # st.write('main_project_R')
        # main_project_C(time_zone_select)
        main_project_U()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    if get_status_by_name('main_project_D'):
        # st.write(get_status_by_name(df_display, 'sub_log'))
        main_project_D()
        # st.write(get_status_by_name(df_display, 'sub_select_item_and_CRUD'))
    else:
        pass
    
    
    
    
    
    # ----------
    
    form_placeholder = st.sidebar.empty()  #
    
    with form_placeholder.form(key='Show data'):
    
        # st.sidebar.button("Retry")
        submit_button = st.form_submit_button('Show data')
    if submit_button:
        
        st.write('#### User data')
        
        st.table(st.session_state.user_data)
       
        response = requests.get(API_URL_users)
        st.write(response.status_code)
        st.table(response.json())
        
        st.write('#### Link data')
        
        st.table(st.session_state.link_data)
       
        response = requests.get(API_URL_links)
        st.write(response.status_code)
        st.table(response.json())
        
        st.write('#### Meeting data')
        
        st.table(st.session_state.meeting_data)
        
        response = requests.get(API_URL_meetings)
        st.write(response.status_code)
        st.table(response.json())
        
        st.write('#### Project data')
        
        st.table(st.session_state.project_data)
        
        response = requests.get(API_URL_projects)
        st.write(response.status_code)
        st.table(response.json())
        # st.write(response.json())
        
    # ----------
    
    form_placeholder = st.sidebar.empty()  #
    
    with form_placeholder.form(key='Show chart'):
    
        # st.sidebar.button("Retry")
        submit_button = st.form_submit_button('Show chart')
    if submit_button:
        
        st.write('#### Project chart')
        
        # st.table(st.session_state.user_data)
       
        # response = requests.get(API_URL_users)
        # st.write(response.status_code)
        # st.table(response.json())
        
        # st.write('#### Link data')
        
        # st.table(st.session_state.link_data)
       
        # response = requests.get(API_URL_links)
        # st.write(response.status_code)
        # st.table(response.json())
        
        # st.write('#### Meeting data')
        
        # st.table(st.session_state.meeting_data)
        
        # response = requests.get(API_URL_meetings)
        # st.write(response.status_code)
        # st.table(response.json())
        
        st.write('#### Project data')
        
        st.table(st.session_state.project_data)
        
        response = requests.get(API_URL_projects)
        st.write(response.status_code)
        st.table(response.json())
        # st.write(response.json())
        
        # pass
        
    st.sidebar.table(st.session_state['display_data'])
    # --------------------
    # --------------------
         
# difinition of functions        
# ----------------------------------------------------   already

def time_zone():
    time_zone_list = st.session_state['time_zone']['city']
    time_zone_select = st.sidebar.selectbox('time_zone', time_zone_list)

    # if st.sesog(df_user)
def sub_log(df_display, df_user):
    form_placeholder = st.sidebar.empty()  # Use a placeholder in the sidebar

    # Create the form inside the placeholder
    with form_placeholder.form(key='log_in_or_sign_in'):
        # name = st.text_input('Name_4')
        st.error("Please Log in / sign in")
        log_in_or_sign_in_list = ['Log in', 'Sign in']
        selector = st.selectbox('action', log_in_or_sign_in_list)
        new_name = st.text_input('name', value = 'Tanaka')
        new_mail_add = st.text_input('mail_add', value = 'B')
        new_pw = st.text_input('pw', value = '2')
        
        submit_button = st.form_submit_button('Submit')

    # Condition to check if the form has been submitted
    if submit_button:
        # st.write('Button click!')
        
        
        if selector == 'Log in':
       
            form_placeholder.empty()        
        
            if check_log_in(new_name, new_mail_add, new_pw) == True:
                # st.sidebar.success(f'Log in already under {new_name} name')
                df_display.loc[df_display['name'] == 'sub_log', 'status'] = False
                df_display.loc[df_display['name'] == 'sub_select_item_and_CRUD', 'status'] = True
                st.session_state['display_data'] = df_display
                st.session_state['log_in_mail'] = new_mail_add
                st.session_state['log_in_id'] = get_id_by_mail(new_mail_add)
                
            # fail to log in    
            elif check_log_in(new_name, new_mail_add, new_pw) == False:
                st.sidebar.error('No such user name')
                
        elif selector == 'Sign in':
            
            form_placeholder.empty()        
            
            # st.write('heck_mail_add_double_register(new_mail_add))
            if check_mail_add_double_register(new_mail_add):
                # df_new= pd.DataFrame(st.session_state['user_data'])
    
                
                
                data = {'name': new_name,
                        'mail_add': new_mail_add,
                        'pw': new_pw,
                        }
                
                response = requests.post(API_URL_users, json.dumps(data))
                # st.sidebar.success(f'Log in already under {new_name} name')
                
                df_display.loc[df_display['name'] == 'sub_log', 'status'] = False
                df_display.loc[df_display['name'] == 'sub_select_item_and_CRUD', 'status'] = True
                st.session_state['display_data'] = df_display
                
                st.session_state['log_in_mail'] = new_mail_add
                st.session_state['log_in_id'] = get_id_by_mail(new_mail_add)
                

                
            else:
                st.sidebar.error('Mail address was already uesd')
                
                # st.write('okokok')
        
            
def sub_select_item_and_CRUD(df_display, df_user):
    # -----------------------------------------
    form_placeholder = st.sidebar.empty()  # Use a placeholder in the sidebar

    # Create the form inside the placeholder
    with form_placeholder.form(key='sub_select_item_and_CRUD'):
        name = get_name_by_mail(st.session_state.log_in_mail)
        st.success(f'Log in under {name}')
        # st.success(f'Log in under {st.session_state.log_in_mail}')
        
        item_list = ['Link', 'Meeting', 'Project']
        item = st.selectbox('Item', item_list)
        action_list = ['Create', 'Read', 'Update', 'Delete', 'Log out']
        action = st.selectbox('Action', action_list)
        
        submit_button = st.form_submit_button('Submit')

    # Condition to check if the form has been submitted
    if submit_button:
        # st.write('Button click!')
        
        if action == 'Log out':
            form_placeholder.empty()          # if selector == "Log in":
            st.write('Log out')
            
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'sub_log', 'status'] = True
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'sub_select_item_and_CRUD', 'status'] = False
            # df_display.loc[df_display['name'] == 'sub_select_item_and_CRUD', 'status'] = False
            # st.session_state['display_data'] = df_display
                
            st.session_state['log_in_mail'] = None
            st.session_state['log_in_id'] = None
                      
        elif item == 'Link':
            if action =='Create':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_C', 'status'] = True
            
            elif action =='Read':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_R', 'status'] = True
            
            elif action =='Update':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_U', 'status'] = True
            
            elif action =='Delete':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_D', 'status'] = True
            
        elif item == 'Meeting':
            if action =='Create':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_C', 'status'] = True
            
            elif action =='Read':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_R', 'status'] = True
            
            elif action =='Update':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_U', 'status'] = True
            
            elif action =='Delete':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_D', 'status'] = True         
                
        elif item == 'Project':
            if action =='Create':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_C', 'status'] = True
            
            elif action =='Read':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_R', 'status'] = True
            
            elif action =='Update':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_U', 'status'] = True
            
            elif action =='Delete':
               
                st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_D', 'status'] = True         
            
        # elif item == 'Meeting':
            
    # -----------------------------------------
def main_link_C(category_list, status_list):
    form_placeholder = st.empty()  # Use a placeholder in the sidebar
       
    # with st.form(key='create_link'):
    with form_placeholder.form(key='main_link_C'):
        
        st.subheader('Create Link Information')
        new_name = st.text_input('Name')
        new_url = st.text_input('URL')
        # category_list = ['Private', 'Public', 'Company']
        new_category = st.selectbox('Category', category_list)
        # status_list = ['Open', 'Public', 'Private', 'Secret']
        new_status = st.selectbox('Status', status_list)
        df_new = pd.DataFrame({'name': [new_name], 'url': [new_url], 'category': [new_category], 'status': [new_status], 'id_user': [st.session_state['log_in_mail']]})
        submit_button = st.form_submit_button(label='Create')

        if submit_button:
            
            data = {'name': new_name,
                'url': new_url,
                'category': new_category,
                'status': new_status,
                # 'mail_add': st.session_state['log_in_mail'],
                'id_user': st.session_state['log_in_id'],
                }
            
            # st.write(i)
            response = requests.post(API_URL_links, json.dumps(data))
            
            st.session_state['link_data'] = pd.concat([st.session_state['link_data'], df_new])
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_C', 'status'] = False
            form_placeholder.empty()        

    # st.table(st.session_state['link_data'])
def main_link_R():
    
    form_placeholder = st.empty()  # Use a placeholder in the sidebar
    
    st.table(st.session_state['link_data'])
    
    response = requests.get(API_URL_links)
    st.write('User / sqlite')
    st.write(response.status_code)
    st.table(response.json())
    # st.table(pd.DataFrame(response.json()))
    
    
    st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_R', 'status'] = False
    
    form_placeholder.empty()      
    # st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_R', 'status'] = False
       
    # st.table(st.session_state['link_data']) New name
    

def main_link_U(category_list, status_list):
    
    response = requests.get(API_URL_links)
    list_id = response.json()
    min_id = list_id[0]['id']
    
    # category_list = ['Private', 'Public', 'Company']
    # status_list = ['Open', 'Public', 'Private', 'Secret']
    
    
    st.subheader("Update Link Information")
    data_id = st.number_input("Enter the ID of the user to update", min_value=min_id, step=1)

    form_placeholder = st.empty()  # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_link_U_1'):
    # Display subheader and selectbox outside the form
        
        response = requests.get(f"{API_URL_links}{data_id}")
        if response.status_code == 200:
            link_data = response.json()
            name = link_data['name']
            url = link_data['url']
            
            status = link_data['status']
            # df_new = pd.DataFt.form_submit_button(label='Create')
            category = link_data['category']
            # status = link_datta['mail_add']
            id_user = link_data['id_user']
            
            
            
        else:
            st.error("User not found")
            name = ''
            url = ''
            category = ''
            status = ''
            
        new_name = st.text_input('New name', value=name)  # Assuming you want to show the selected link name as initial value
        new_url = st.text_input('New URL', value=url)
        new_category = st.selectbox('New Category', category_list)
        # new_status = st.selectbox('Status', value=status)
        new_status = st.selectbox('Status', status_list)
            
        data = {
            'name': new_name, 
            'url': new_url, 
            'category': new_category, 
            'status': new_status, 
            'id_user': id_user
            
        }
            
        st.write(response.status_code)
        
        # st.table(pd.DataFrame(response.json())['name'])
        
        
        submit_button = st.form_submit_button(label='Update Link')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
            response = requests.put(f"{API_URL_links}{data_id}", json.dumps(data))
            if response.status_code == 200:
                st.success("User updated successfully")
            else:
                st.error("An error occurred")
                st.write(response.status_code)
   
            # st.session_state['link_data'].loc[st.session_state['link_data']['name'] == link_name] = df_new
            
            response = requests.get(API_URL_links).json()
            df = pd.DataFrame(response)
            
            
            
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_U', 'status'] = False
            form_placeholder.empty()  # Clear the form
            
def main_link_D():
    # category_list = ['Private', 'Public', 'Company']
    # status_list = ['Open', 'Public', 'Private', 'Secret']
    
    response = requests.get(API_URL_links)
    list_id = response.json()
    min_id = list_id[0]['id']
    
    # st.write(list_id[0]['id'])

    data_id = st.number_input("Enter the ID of the user to delete", min_value=min_id, step=1)
    form_placeholder = st.empty()  
    # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_link_D'):
    # Display subheader and selectbox outside the form
        st.subheader("Delete Link Information")
        # link_name_list = list(st.session_state['link_data']['name'])
        # link_name = st.selectbox("Link name", link_name_list)
        response = requests.get(f"{API_URL_links}{data_id}")
        if response.status_code == 200:
            user_data = response.json()
            name = user_data['name']
            url = user_data['url']
            
            status = user_data['status']
            # df_new = pd.DataFrame({'name': [new_name], 'url': [new_url], 'category': [new_category], 'status': [new_status], 'mail_add': [st.session_state['log_in_mail']]})
            # submit_button = st.form_submit_button(label='Create')
            category = user_data['category']
            # status = user_data['status']
            id_user = user_data['id_user']
            
            
            
        else:
            st.error("User not found")
            name = ''
            url = ''
            category = ''
            status = ''
            
        new_name = st.text_input('New name', value=name)  # Assuming you want to show the selected link name as initial value
        new_url = st.text_input('New URL', value=url)
        new_category = st.text_input('New Category', value=category)
        # new_status = st.text_input('Status', value=status)
        new_status = st.text_input('Status', value=status)
        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Delete')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
   
            response = requests.delete(f"{API_URL_links}{data_id}")
            if response.status_code == 200:
                st.success("Link deleted successfully")
            else:
                st.error("An error occurred or Link not found")
            # st.session_state['link_data'] = st.session_state['link_data'][st.session_state['link_data']['name'] != link_name]
            
            # st.session_state['link_data'].loc[st.session_state['link_data']['name'] == link_name] = None
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_link_D', 'status'] = False
            form_placeholder.empty()  # Clear the form
            
            
            
# --------------------------------------------------
def main_meeting_C(time_zone_select):
    form_placeholder = st.empty()  # Use a placeholder in the sidebar
    
    time_diff = float(st.session_state['time_zone'].loc[st.session_state['time_zone']['city'] == time_zone_select, 'time'])
    # st.write(time_diff)
    
    # with st.form(key='create_meeting'):
    
        # st.subheader('Create Meeting Information')
    with form_placeholder.form(key='main_meeting_C'):
        st.subheader('Create Meeting Information')
        
       
        new_name = st.text_input('Name')
        new_description = st.text_input('Description')
        category_list = ['Private', 'Public', 'Company']
        new_category = st.selectbox('Category', category_list)
        # category = st.text_input('Category')
        status_list = ['Open', 'Public', 'Private', 'Secret']
        new_status = st.selectbox('Status', status_list)
        date = st.date_input('Input date', min_value=dt.date.today())
        start_time = st.time_input('Start time: ', value=dt.time(hour=9, minute=0))
        end_time = st.time_input('End time: ', value=dt.time(hour=10, minute=0))
        
        
        submit_button = st.form_submit_button(label='Meeting_Create')

        if submit_button:
            
            data = {
                'name': [new_name], 
                'description': [new_description], 
                'category': [new_category], 
                'status': [new_status], 

                'start_datetime': (dt.datetime(
                    year=date.year, 
                    month=date.month,
                    day=date.day,
                    hour=start_time.hour,
                    minute=start_time.minute
                    ) - dt.timedelta(hours = time_diff)).isoformat(),
                'end_datetime': (dt.datetime(
                    year=date.year, 
                    month=date.month,
                    day=date.day,
                    hour=end_time.hour,
                    minute=end_time.minute
                    ) - dt.timedelta(hours = time_diff)).isoformat(),
                'id_user': [st.session_state['log_in_id']]
            }
            
            data_R = {
                'name': new_name, 
                'description': new_description, 
                'category': new_category, 
                'status': new_status, 

                'start_datetime': (dt.datetime(
                    year=date.year, 
                    month=date.month,
                    day=date.day,
                    hour=start_time.hour,
                    minute=start_time.minute
                    ) - dt.timedelta(hours = time_diff)).isoformat(),
                'end_datetime': (dt.datetime(
                    year=date.year, 
                    month=date.month,
                    day=date.day,
                    hour=end_time.hour,
                    minute=end_time.minute
                    ) - dt.timedelta(hours = time_diff)).isoformat(),
                'id_user': st.session_state['log_in_id']
            }
            
            df_new = pd.DataFrame(data)
            
            response = requests.post(API_URL_meetings, json.dumps(data_R))
            
            
            st.session_state['meeting_data'] = pd.concat([st.session_state['meeting_data'], df_new])
            # st.write(response.status_code)
            
            # response = requests.post(API_URL_meetings, json.dumps(data))
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_C', 'status'] = False
            form_placeholder.empty()       
            
            
            
            
            # st.table(st.session_state['meeting_data'])
 
        
# def main_meeting_C(time_zone_select):
      
def main_meeting_R(time_zone_select):
    
    form_placeholder = st.empty()  
    time_diff = float(st.session_state['time_zone'].loc[st.session_state['time_zone']['city'] == time_zone_select, 'time'])
    # st.write(time_diff)# Use a placeholder in the sidebar
    
    # df = pd.DataFrame(st.session_state['meeting_data'])
    st.table(st.session_state['meeting_data'])
    
    
    response = requests.get(API_URL_meetings)
    df = pd.DataFrame(response.json())
    
    df['start_datetime'] = pd.to_datetime(df['start_datetime'])
    df['start_datetime'] = [i + dt.timedelta(hours=time_diff) for i in df['start_datetime']]
    
    df['end_datetime'] = pd.to_datetime(df['end_datetime'])
    df['end_datetime'] = [i + dt.timedelta(hours=time_diff) for i in df['end_datetime']]
    
    st.table(df)
    # st.table(st.session_state['meeting_data'])
    st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_R', 'status'] = False
    
    form_placeholder.empty()      
    
    
def main_meeting_U(time_zone_select):
    
    response = requests.get(API_URL_meetings)
    list_id = response.json()
    min_id = list_id[0]['id']
    
    
    st.write(time_zone_select)
    time_diff = float(st.session_state['time_zone'].loc[st.session_state['time_zone']['city'] == time_zone_select, 'time'])
    st.write(time_diff)
    
    category_list = ['Private', 'Public', 'Company']
    status_list = ['Open', 'Public', 'Private', 'Secret']
    
    st.subheader("Update Meeting Information")
    data_id = st.number_input("Enter the ID of the user to update", min_value=min_id, step=1)
    # meeting_name_list = list(st.session_state['meeting_data']['name'])
    # meeting_name = st.selectbox("meeting name", meeting_name_list)
    
    form_placeholder = st.empty()  # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_meeting_U_1'):
        
        response = requests.get(f"{API_URL_meetings}{data_id}")
        if response.status_code == 200:
            meeting_data = response.json()
            name = meeting_data['name']
            description = meeting_data['description']
            category = meeting_data['category']
            status = meeting_data['status']
            start_datetime = meeting_data['start_datetime']
            end_datetime = meeting_data['end_datetime']
            id_user = meeting_data['id_user']
            
            # df_new = pd.DataFrame({'name': [new_name], 'url': [new_url], 'category': [new_category], 'status': [new_status], 'id_user': [st.session_state['log_in_mail']]})
            # submit_button = st.form_submit_button(label='Create')
            # status = meeting_data['status']
            
            
            
        else:
            st.error("User not found")
            name = ''
            description = ''
            category = ''
            status = ''
            start_datetime = ''
            end_datetime = ''
            id_user = ''
        
        
        
    # Display subheader and selectbox outside the form
        
        
        new_name = st.text_input('Name', value=name)
        new_description = st.text_input('Description', value=description)
        new_category = st.selectbox('Category', category_list)
        # category = st.text_input('Category')
        new_status = st.selectbox('Status', status_list)
        date = st.date_input('Input date', min_value=dt.date.today())
        start_time = st.time_input('Start time: ', value=dt.time(hour=9, minute=0))
        end_time = st.time_input('End time: ', value=dt.time(hour=20, minute=0))    
        
        
        
        
        
        df_new = pd.DataFrame({
            'name': [new_name], 
            'description': [new_description], 
            'category': [new_category], 
            'status': [new_status], 

            'start_datetime': (dt.datetime(
                year=date.year, 
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
                ) - dt.timedelta(hours = time_diff)).isoformat(),
            'end_datetime': (dt.datetime(
                year=date.year, 
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
                ) - dt.timedelta(hours = time_diff)).isoformat(),
            'id_user': [st.session_state['log_in_id']]
        })
 
        data = {
            'name': new_name, 
            'description': new_description, 
            'category': new_category, 
            'status': new_status, 

            'start_datetime': (dt.datetime(
                year=date.year, 
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
                ) - dt.timedelta(hours = time_diff)).isoformat(),
            'end_datetime': (dt.datetime(
                year=date.year, 
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
                ) - dt.timedelta(hours = time_diff)).isoformat(),
            'id_user': st.session_state['log_in_id']
        }
 
        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Update_meeting')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
            
            response = requests.put(f"{API_URL_meetings}{data_id}", json.dumps(data))
            if response.status_code == 200:
                st.success("User updated successfully")
            else:
                st.error("An error occurred")
                st.write(response.status_code)
            
            

            # st.session_state['meeting_data'].loc[st.session_state['meeting_data']['name'] == meeting_name] = df_new
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_U', 'status'] = False
            form_placeholder.empty()  # Clear the form
    
def main_meeting_D():
    
    response = requests.get(API_URL_meetings)
    list_id = response.json()
    min_id = list_id[0]['id']
    
    # category_list = ['Private', 'Public', 'Company']
    # status_list = ['Open', 'Public', 'Private', 'Secret']
    # st.table(st.session_state['time_zone'])
    data_id = st.number_input("Enter the ID of the user to delete", min_value=min_id, step=1)
    
    form_placeholder = st.empty()  # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_meeting_D'):
    # Display subheader and selectbox outside the form
        st.subheader("Delete Meeting Information")
        # meeting_name_list = list(st.session_state['meeting_data']['name'])
        # meeting_name = st.selectbox("Meeting name", meeting_name_list)
        response = requests.get(f"{API_URL_meetings}{data_id}")
        if response.status_code == 200:
            meeting_data = response.json()
            name = meeting_data['name']
            description = meeting_data['description']
            category = meeting_data['category']
            status = meeting_data['status']
            start_datetime = meeting_data['start_datetime']
            end_datetime = meeting_data['end_datetime']
            # df_new = pd.DataFrame({'name': [new_name], 'url': [new_url], 'category': [new_category], 'status': [new_status], 'mail_add': [st.session_state['log_in_mail']]})
            # submit_button = st.form_submit_button(label='Create')
            # status = meeting_data['status']
            id_user = meeting_data['id_user']
            
        else:
            st.error("Meeting not found")
            name = ''
            description = ''
            
        new_name = st.text_input('New name', value=name)
        new_description = st.text_input('New description', value=description)

        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Delete')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
            
            response = requests.delete(f"{API_URL_meetings}{data_id}")
            if response.status_code == 200:
                st.success("Meeting deleted successfully")
            else:
                st.error("An error occurred or Meeting not found")
            # Assuming you want to update an existing link rather than creating a new one
            # This part needs logic to update the existing link data instead of just appending
            # For now, it's appending to demonstrate functionality
            # st.session_state['meeting_data'] = st.session_state['meeting_data'][st.session_state['meeting_data']['name'] != meeting_name]
            
            # st.session_state['link_data'].loc[st.session_state['link_data']['name'] == link_name] = None
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_D', 'status'] = False
            form_placeholder.empty()  # Clear the form
       
            
# --------------------------------------------------
# --------------------------------------------------
def main_project_C():
    form_placeholder = st.empty()  # Use a placeholder in the sidebar
    
    # time_diff = float(st.session_state['time_zone'].loc[st.session_state['time_zone']['city'] == time_zone_select, 'time'])
    # st.write(time_diff)
    
    # with st.form(key='create_project'):
    with form_placeholder.form(key='main_project_C'):
        st.subheader("Create Project Information")
        new_name = st.text_input('Name')
        country_list = ['Singapore', 'Malaysia', 'Indonesia', 'Thai', 'Philippines', 'China', 'Hong Kong', 'Taiwan', 'India', 'Bangladesh']
        
        new_country = st.selectbox('Country', country_list)
        new_client = st.text_input('Client')
        type_of_building_list = ['Factory', 'Warehouse', 'Office', 'Data_center']
        new_type_of_building = st.selectbox('Type_of_building', type_of_building_list)
        new_total_floor_area = st.text_input('Total_floor_area')
        new_m_amount = st.text_input('M_amount')
        
        currency_list = ['USD', 'JPY', 'SGD', 'RM', 'IRP']
        new_currency = st.selectbox('Currency', currency_list)
        new_date_of_submission = st.date_input('Input date', min_value=dt.date.today())
        
        submit_button = st.form_submit_button(label='project_Create')

        if submit_button:
            
            data = {
                'name': [new_name], 
                'country': [new_country], 
                'client': [new_client], 
                'type_of_building': [new_type_of_building], 
                'total_floor_area': [new_total_floor_area], 
                'm_amount': [new_m_amount], 
                'currency': [new_currency], 
                'type_of_building': [new_type_of_building], 

                # 'date_of_submission': [new_date_of_submission],
                
                'date_of_submission': (dt.date(
                    year=new_date_of_submission.year, 
                    month=new_date_of_submission.month,
                    day=new_date_of_submission.day,
                    )).isoformat(),
                
                
                
                
                
                'id_user': [st.session_state['log_in_id']]
            }
            
            data_R = {
                'name': new_name, 
                'country': new_country, 
                'client': new_client, 
                'type_of_building': new_type_of_building, 
                'total_floor_area': new_total_floor_area, 
                'm_amount': new_m_amount, 
                'currency': new_currency, 
                'type_of_building': new_type_of_building, 

                # 'date_of_submission': new_date_of_submission.isoformat(),
                'date_of_submission': (dt.date(
                    year=new_date_of_submission.year, 
                    month=new_date_of_submission.month,
                    day=new_date_of_submission.day,
                    )).isoformat(),
                
                'id_user': st.session_state['log_in_id'],
            }
            
            
            
            df_new = pd.DataFrame(data)
            
            response = requests.post(API_URL_projects, json.dumps(data_R))
            
            
            st.session_state['project_data'] = pd.concat([st.session_state['project_data'], df_new])
            # st.write(response.status_code)
            
            # response = requests.post(API_URL_projects, json.dumps(data))
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_C', 'status'] = False
            form_placeholder.empty()       
            
            
def main_project_R(time_zone_select):
    
    form_placeholder = st.empty()  
    time_diff = float(st.session_state['time_zone'].loc[st.session_state['time_zone']['city'] == time_zone_select, 'time'])
    # st.write(time_diff)# Use a placeholder in the sidebar
    
    # df = pd.DataFrame(st.session_state['project_data'])
    st.table(st.session_state['project_data'])
    
    
    response = requests.get(API_URL_projects)
    df = pd.DataFrame(response.json())
    
    # df['start_datetime'] = pd.to_datetime(df['start_datetime'])
    # df['start_datetime'] = [i + dt.timedelta(hours=time_diff) for i in df['start_datetime']]
    
    # df['end_datetime'] = pd.to_datetime(df['end_datetime'])
    # df['end_datetime'] = [i + dt.timedelta(hours=time_diff) for i in df['end_datetime']]
    
    st.table(df)
    # st.table(st.session_state['project_data'])
    st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_meeting_R', 'status'] = False
    
    form_placeholder.empty()                
            
    
def main_project_U():
    
    response = requests.get(API_URL_projects)
    list_id = response.json()
    min_id = list_id[0]['id']
   
    
    st.subheader("Update project Information")
    data_id = st.number_input("Enter the ID of the user to update", min_value=min_id, step=1)
    
    form_placeholder = st.empty()  # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_project_U_1'):
        
        response = requests.get(f"{API_URL_projects}{data_id}")
        if response.status_code == 200:
            project_data = response.json()
            
            
            name = project_data['name']
            country = project_data['country']
            client = project_data['client']
            type_of_building = project_data['type_of_building']
            # start_datetime = project_data['start_datetime']
            total_floor_area = project_data['total_floor_area']
            m_amount = project_data['m_amount']
            currency = project_data['currency']
            # type_of_building= project_data['type_of_building']
            date_of_submission = project_data['date_of_submission']
            # end_datetime = project_data['end_datetime']
            id_user = project_data['id_user']
            
            
            
            
            
        else:
            st.error("User not found")
            # naser = ''
            
            name = ''
            country = ''
            client = ''
            type_of_building = ''
            # start_datetime = ''
            total_floor_area = ''
            m_amount = ''
            currency = ''
            type_of_building= ''
            date_of_submission = ''
            # end_datetime = ''
            id_user = ''
        
        
        
    # Display subheader and selectbox outside the form
        
        
        
        st.write((date_of_submission))
        
        
        date_of_submission = dt.datetime.strptime(date_of_submission, '%Y-%m-%d').date()# new_id_user = st.text_input('', value=name)
        
        new_name = st.text_input('Name', value=name)
        country_list = ['Singapore', 'Malaysia', 'Indonesia', 'Thai', 'Philippines', 'China', 'Hong Kong', 'Taiwan', 'India', 'Bangladesh']
        
        new_country = st.text_input('Country', value=country)
        new_client = st.text_input('Client', value=client)
        new_type_of_building = st.text_input('Typr of biulding', value=type_of_building)
        new_total_floor_area = st.text_input('Total floor area', value=total_floor_area)
        new_m_amount = st.text_input('M amount', value=m_amount)
        new_currency = st.text_input('Currency', value=currency)
        new_date_of_submission = st.date_input('Date of submission', value=date_of_submission)
        # from datetime import datetime

# Assuming date_of_submission is a string in 'YYYY-MM-DD' format
        
        
        
        
        
        df_new = pd.DataFrame({
            'name': [new_name], 
            'country': [new_country], 
            'client': [new_client], 
            'type_of_building': [new_type_of_building], 
            'total_floor_area': [new_total_floor_area], 
            'm_amount': [new_m_amount], 
            'currency': [new_currency], 
            'type_of_building': [new_type_of_building], 
            

            # 'date_of_submission': [new_date_of_submission],
            'date_of_submission': (dt.date(
                year=new_date_of_submission.year,
                month=new_date_of_submission.month,
                day=new_date_of_submission.day,
            )).isoformat(),
            
            'id_user': [st.session_state['log_in_id']]
        })
 
        data = {
            'name': new_name, 
            'country': new_country, 
            'client': new_client, 
            'type_of_building': new_type_of_building, 
            'total_floor_area': new_total_floor_area, 
            'm_amount': new_m_amount, 
            'currency': new_currency, 
            'type_of_building': new_type_of_building, 

            'date_of_submission': new_date_of_submission.isoformat(),
            
            
            'id_user': st.session_state['log_in_id']
        }
 
        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Update_project')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
            
            response = requests.put(f"{API_URL_projects}{data_id}", json.dumps(data))
            st.write(response.status_code)
            if response.status_code == 200:
                st.success("User updated successfully")
            else:
                st.error("An error occurred")
                st.write(response.status_code)
            
            

          




            
                       
def main_project_D():
    
    response = requests.get(API_URL_projects)
    list_id = response.json()
    min_id = list_id[0]['id']
    
    # category_list = ['Private', 'Public', 'Company']
    # status_list = ['Open', 'Public', 'Private', 'Secret']
    # st.table(st.session_state['time_zone'])
    data_id = st.number_input("Enter the ID of the user to delete", min_value=min_id, step=1)
    
    form_placeholder = st.empty()  # Use a placeholder in the main area, not the sidebar as previously mentioned
    # Create the form inside the placeholder
    with form_placeholder.form(key='main_project_D'):
    # Display subheader and selectbox outside the form
        st.subheader("Delete Project Information")
        # meeting_name_list = list(st.session_state['meeting_data']['name'])
        # meeting_name = st.selectbox("Meeting name", meeting_name_list)
        response = requests.get(f"{API_URL_projects}{data_id}")
        if response.status_code == 200:
            project_data = response.json()
            name = project_data['name']
            country = project_data['country']
            client = project_data['client']
            type_of_building = project_data['type_of_building']
            total_floor_area = project_data['total_floor_area']
            
            m_amount = project_data['m_amount']
            currency = project_data['currency']
            
            
            date_of_submission = project_data['date_of_submission']
            id_user = project_data['id_user']
            
        else:
            st.error("Project not found")
            
            
          
            
            name = ''
            country = ''
            client = ''
            type_of_building = ''
            # start_datetime = ''
            total_floor_area = ''
            m_amount = ''
            currency = ''
            type_of_building= ''
            date_of_submission = ''
            # end_datetime = ''
            id_user = ''
            
        # st.write(response.status_code)
        # st.write((date_of_submission))
        
        date_of_submission = dt.datetime.strptime(date_of_submission, '%Y-%m-%d').date()# new_id_user = st.text_input('', value=name)
        
        new_name = st.text_input('Name', value=name)
        new_country = st.text_input('Country', value=country)
        new_client = st.text_input('Client', value=client)
        new_type_of_building = st.text_input('Typr of biulding', value=type_of_building)
        new_total_floor_area = st.text_input('Total floor area', value=total_floor_area)
        new_m_amount = st.text_input('M amount', value=m_amount)
        new_currency = st.text_input('Currency', value=currency)
        new_date_of_submission = st.date_input('Date of submission', value=date_of_submission)
            
      

        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Delete')  # Changed label to 'Update' to reflect the action

        # Actions to take if the form is submitted
        if submit_button:
            
            response = requests.delete(f"{API_URL_projects}{data_id}")
            if response.status_code == 200:
                st.success("Project deleted successfully")
            else:
                st.error("An error occurred or Project not found")
           
            st.session_state['display_data'].loc[st.session_state['display_data']['name'] == 'main_project_D', 'status'] = False
            form_placeholder.empty()  # Clear the form

    
            
        
def check_log_in(new_name, new_mail_add, new_pw):
    
    #------------------------------------

    
    response = requests.get(API_URL_users)
    response = response.json()
    df = pd.DataFrame(response)
    # st.table(df['name'])
    # st.write(response[0]['name'])
    
    if df['mail_add'].isin([new_mail_add]).any():
        if df.loc[df['mail_add'] == new_mail_add]['name'].values == new_name:
            if df.loc[df['mail_add'] == new_mail_add]['pw'].values == new_pw:
                return True
            else: 
                return False
        # If any() returns True, it means the mail address already exists           
        else:
            return False
    else:
        # If the mail address does not exist, return True
        return False
    
    
        
    # st.write(new_name)
    
def get_status_by_name(name):
    # Find the status for the given name
    # df = st.session_state['display_data']
    status = st.session_state['display_data'].loc[st.session_state['display_data']['name'] == name, 'status'].values

    return status


def get_name_by_mail(mail_add):
    # df = pd.DataFrame(st.session_state.user_data)
    response = requests.get(API_URL_users)
    response = response.json()
    df = pd.DataFrame(response)
    # name = st.session_state.user_data.loc[st.session_state.user_data['mail_add'] == mail_add, 'name'].values[0]
    # name = st.session_state.user_data.loc[st.session_state.user_data['mail_add'] == mail_add, 'name'].values
    # name = df.loc[df['mail_add'] == mail_add, 'name'].values[0]
    name = df.loc[df['mail_add'] == mail_add, 'name'].values
    if name:
        name = name[0]
    return name

def get_id_by_mail(mail_add):
    # df = pd.DataFrame(st.session_state.user_data)
    response = requests.get(API_URL_users)
    response = response.json()
    df = pd.DataFrame(response)
    # name = st.session_state.user_data.loc[st.session_state.user_data['mail_add'] == mail_add, 'name'].values[0]
    # name = st.session_state.user_data.loc[st.session_state.user_data['mail_add'] == mail_add, 'name'].values
    # name = df.loc[df['mail_add'] == mail_add, 'name'].values[0]
    id = df.loc[df['mail_add'] == mail_add, 'id'].values
    if id:
        id = id[0]
    return int(id)

            
def check_mail_add_double_register(mail_add):
    
    response = requests.get(API_URL_users)
    response = response.json()
    df = pd.DataFrame(response)
    # st.table(df['name'])
    # Check if the mail_add exists in the 'mail_add' column of the user_data DataFrame
    # if st.session_state.user_data['mail_add'].isin([mail_add]).any():
    if df['mail_add'].isin([mail_add]).any():
        # If any() returns True, it means the mail address already exists
        return False
    else:
        # If the mail address does not exist, return True
        return True  

        
if __name__ == '__main__':
    main()     
        
        
        
        



    