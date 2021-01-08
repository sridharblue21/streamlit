import streamlit as st
import stapp # import sub-module stapp
from load_css import local_css
import login
import authenticate
import popular_reco
import menu

local_css("style.css") # include style.css

def print_hi(name):
    welcome_head=f"<div>Hi <span class='highlight blue'>{name}</span>, Welcome!</div>"
    st.markdown(welcome_head,unsafe_allow_html=True)

def main():
    yourname,yourpass=login.login() #get login field values
    st.header('Top Songs Recommender System ')
    message=authenticate.authenticate(yourname,yourpass)
    # authenticate with name,passcode not empty and passcode matching
    if message == 'authenticated': # display blocks below if authenticated
        print_hi(yourname)
        st.write ('\n')
        menu_out=menu.menu()

        if menu_out=='Artist Choice':
            # menu_mesg=stapp.func_welcome(menu_out,1)# call welcome function from the sub-module
            # st.markdown(menu_mesg, unsafe_allow_html=True)
            pop=popular_reco.artist_choice()
            if pop:
                pop_msg=f"<div>Your favourite(s), <span class='highlight blue'>{pop}</span></div>"
                st.markdown(pop_msg,unsafe_allow_html=True)
            st.write('\n')
        elif menu_out=='Popular Titles':
            # menu_mesg=stapp.func_welcome(menu_out,1)# call welcome function from the sub-module
            # st.markdown(menu_mesg, unsafe_allow_html=True)

            #sub_menu popularity menus
            sub_menu_out=menu.submenu_1()
            if sub_menu_out=='Most Played':
                # sub_menu_mesg = stapp.func_welcome(sub_menu_out,2)  # call welcome function from the sub-module
                # st.markdown(sub_menu_mesg, unsafe_allow_html=True)
                st.write('\n')
                n=st.slider('Select how many song recommendations you would need?',min_value=2, max_value=10)
                top_pop_songs_title = stapp.top_pop_songs(n)# call popular songs function top-5
                st.subheader(f"Most played titles, {n} recommendations for you")
                st.spinner()
                with st.spinner(text='In progress'):
                    st.table(top_pop_songs_title)
                    st.success('Done')
            elif sub_menu_out == 'Most Rated':
                #sub_menu_mesg = stapp.func_welcome(sub_menu_out,2)
                #st.markdown(sub_menu_mesg, unsafe_allow_html=True)
                st.write('\n')
                region=st.selectbox('Choose your region',options=['IN','US','/N'])
                if region:
                    n=st.slider('Select how many song recommendations you would need?',min_value=2, max_value=10)
                    top_rated_songs_title = stapp.top_rated_songs(n, region)  # call popular songs function top-5
                    st.subheader(f"Most rated titles, {n} recommendations for you")
                    st.write(id)
                    st.spinner()
                    with st.spinner(text='In progress'):
                        st.table(top_rated_songs_title)
                        st.success('Done')
                else:
                    st.write('Choose your region')
            st.write('\n')
    else:
        st.sidebar.markdown(message,unsafe_allow_html=True)

# call main function here
if __name__ == '__main__':
    main()
