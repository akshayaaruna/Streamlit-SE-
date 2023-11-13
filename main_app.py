import streamlit as st
from home_page import run_home_page
from data_exploration_page import run_data_exploration_page
from prediction_page import run_prediction_page
from contact_page import run_contact_page
from streamlit_option_menu import option_menu
from login import login, is_user_allowed

def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",
                options=["Home", "Data Exploration", "Prediction", "Contact"],
                icons=["house", "Graph up arrow", "book", "envelope"],
                menu_icon="cast",
                default_index=0,
            )
        return selected

def run_main_app(username, selected_page):
    st.success(f"Access granted for user: {username}")

    # Continue with the main application based on user selection
    if selected_page == "Home":
        run_home_page()
    elif selected_page == "Data Exploration":
        run_data_exploration_page()
    elif selected_page == "Prediction":
        run_prediction_page()
    elif selected_page == "Contact":
        run_contact_page()

def main():
    # Check if the user is already logged in
    is_logged_in = st.session_state.get('is_logged_in', False)
    
    if not is_logged_in:
        success, username = login()

        if success:
            # Check if the authenticated user is allowed access
            if is_user_allowed(username):
                st.session_state.is_logged_in = True  # Set the login status in the session state
                st.success(f"Access granted for user: {username}")

                # Continue with the main application based on user selection
                selected_page = streamlit_menu(1)
                run_main_app(username, selected_page)
            else:
                st.error(f"Access denied for user: {username}")
        else:
            st.warning("Please login to access the application.")
    else:
        # User is already logged in, display the main application
        selected_page = streamlit_menu(1)
        run_main_app("", selected_page)  # Pass an empty string or None as the username if it's not needed

if __name__ == '__main__':
    main()
