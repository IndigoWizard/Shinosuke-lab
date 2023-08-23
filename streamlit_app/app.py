import streamlit as st

def user_card(user_name, contact_info, image_path):
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(image_path, width=200)
    with col2:
        st.markdown(f"### {user_name}")
        st.markdown(contact_info.replace("\n", "<br>"), unsafe_allow_html=True)

def run():
    st.title("User Card App")
    
    
    user_name = "Shin-chan"
    contact_info = "Email: shinchan@example.com\nPhone: 123-456-7890"
    image_path = "./data/shinchan-square.jpg"
    
    st.subheader("Square image")
    user_card(user_name, contact_info, image_path)
    
    user_name_round = "Square Shin-chan turned Round"
    contact_info_round = "Email: shinchan@example.com\nPhone: 987-654-3210"
    image_path_round = "./data/shinchan-round.jpg"
    
    st.subheader("Square image turned Round")
    user_card(user_name_round, contact_info_round, image_path_round)

    st.write("The square images are better off made round through border-radius than being cropped with a div that's configured for rectangular images.")

    user_name_round = "Shinosuke taking the train - Rectangle"
    contact_info_round = "Email: shinchan@example.com\nPhone: 147-258-369"
    image_path_round = "./data/shinchan-rectangle.jpg"
    
    st.subheader("Rectangle image turned Round (200x300)")
    user_card(user_name_round, contact_info_round, image_path_round)

    user_name_round = "Action Kamen Rectangle"
    contact_info_round = "Email: shinchan@example.com\nPhone: 963-258-741"
    image_path_round = "./data/action-kamen.jpg"
    
    st.subheader("Rectangle image turned Round (200x300)")
    user_card(user_name_round, contact_info_round, image_path_round)

    user_name_round = "Shinosuke Kamen Rectangle"
    contact_info_round = "Email: shinchan@example.com\nPhone: 321-654-987"
    image_path_round = "./data/shinosuke-kamen.jpg"
    
    st.subheader("Rectangle image turned Round (200x300)")
    user_card(user_name_round, contact_info_round, image_path_round)

    user_name_round = "Action Kamen & Shinosuke Kamen - Rectangle"
    contact_info_round = "Email: shinchan@example.com\nPhone: 789-456-123"
    image_path_round = "./data/action-kamen-shinosuke.jpg"
    
    st.subheader("Rectangle image turned Round (200x300)")
    user_card(user_name_round, contact_info_round, image_path_round)

    st.markdown("""
    <style>
        /* main div class */
        .css-1v0mbdj {
            width: 200px;
            height: 200px;
            position: relative;
            overflow: hidden;
            border-radius: 50%;
        }

        /*img elemnt in main div class*/
        .css-1v0mbdj > img{
            display: inline;
            margin: 0 auto;
            margin-top: -35%;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()
