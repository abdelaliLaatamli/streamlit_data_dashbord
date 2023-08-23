def set_sidebar(st):
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 200px !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.image("./assets/img/pls.png" , caption="Online Analytics")

    st.sidebar.header("Choose your filter")