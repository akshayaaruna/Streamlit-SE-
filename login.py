import streamlit as st

# Define a dictionary of allowed users and their corresponding passwords
allowed_users = {
    "Store Manager": "Garments",
    "Sales Team": "Garments",
    # Add more users as needed
}

# Function to authenticate user credentials
def authenticate(username, password):
    return username in allowed_users and password == allowed_users[username]

# Function to display the login page
def login():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            return True, username  # Return the authenticated username
        else:
            st.error("Invalid username or password")
    return False, None  # Return a default value when authentication fails

# Function to check if a user is allowed access
def is_user_allowed(username):
    return username in allowed_users

# Main function
def main():
    success, username = login()

    if success:
        # Check if the authenticated user is allowed access
        if is_user_allowed(username):
            st.success(f"Access granted for user: {username}")
            # Continue with the main application
            # (Include your existing main application logic here)
        else:
            st.error(f"Access denied for user: {username}")

if __name__ == '__main__':
    main()
