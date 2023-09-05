import streamlit as st
import streamlit.components.v1 as components

def user_card(user_text, user_context, image_path, iframe_src, html_src):
    col1, col2 = st.columns([1, 2])  # Adjust column ratios as needed
    with col1:
        st.image(image_path, width=200)
    with col2:
        st.markdown(f"#### {user_text}")
        st.write(user_context)  # Using st.write for text content
        if iframe_src:
            components.iframe(iframe_src)
        if html_src:
            components.html(html_src, height=320, width=450, scrolling=False)

def run():
    with st.sidebar:
        st.title("Shin-chan Lab")
        st.markdown("![](https://www.pixenli.com/image/fm0aEpMI)", unsafe_allow_html=True)
    
    st.title("Shinosuke to the rescue!")
    st.markdown("#### Welcome to Shinosuke's Lab, where Shin-chan demos solutions to Streamlit users in need of help!")
    st.markdown("In today's lesson, we learn how to embeed Iframes and HTML elments in Streamlit.<br> It is important to note that both of these elements are generally not advised; iframes can be used in Streamlit to embeed maps like in folium-streamlit package where Folium maps are generated as iframes since they are based of LeafletJS maps.<br>HTML elements on the other hand are tricky and may be blocked by the browser itself even if Streamlit allows it to runn so it's up to you to figure a way around it.", unsafe_allow_html=True)
    # First Example
    text = "Shinosuke is taking the train, he surely will be listening to music during his long voyage!"
    context = "Shin-chan is now listening to:"
    iframe_src = "https://open.spotify.com/embed/track/59BweHnnNQc5Y55WO30JuK?utm_source=generator"
    image_path = "data/shinchan-rectangle.jpg"
    
    user_card(text, context, image_path, iframe_src, None)

    # Embeded Iframe Component Implementation
    st.code(
        """
        import streamlit as st
        import streamlit.components.v1 as components
        
        def run():
            iframe_src = "https://open.spotify.com/embed/track/59BweHnnNQc5Y55WO30JuK?utm_source=generator"
            components.iframe(iframe_src)
        
        if __name__ == "__main__":
            run()
        """,
        language='python'
    )

    st.divider()

    # Second Example
    st.subheader("It turns out shinosuke was goign to the gym, I wonder what he listens to while working out, humm...")
    text = "Shinosuke is muscling up! He works out hard and keeps a disciplined schedule."
    context = "Shin-chan listens to a different genre of music to get hyped up and motivate his body for extra hard work, he listens to:"
    html_src = """
        <iframe width="450" height="280" src="https://www.youtube.com/embed/3QyVHDclDME?si=Ir0zLb6tvxyLey4E&amp;start=28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        """
    image_path = "data/shinchan-square.jpg"
    
    user_card(text, context, image_path, None, html_src)

    # Embeded HTML Component Implementation
    st.code(
        """
        import streamlit as st
        import streamlit.components.v1 as components
        
        def run():
            html_src = \"\"\"<iframe width="450" height="280" src="https://www.youtube.com/embed/3QyVHDclDME?si=Ir0zLb6tvxyLey4E&amp;start=28" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\"\"\"
            components.html(html_src, height=320, width=450, scrolling=False)
        
        if __name__ == "__main__":
            run()
        """,
        language='python'
    )

    ### App Custom CSS
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

        /* img element in main div class */
        .css-1v0mbdj > img {
            display: inline;
            margin: 0 auto;
            margin-top: -35%;
        }
        div.css-ocqkz7:nth-child(8) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > img:nth-child(1) {
            margin-top: 0;
        }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()
