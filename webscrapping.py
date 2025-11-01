import streamlit as st
import requests
from io import BytesIO
from dotenv import load_dotenv
import os 

load_dotenv()
ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

st.markdown("<h1 style='color: red;'>📸 Image Generator</h1>", unsafe_allow_html=True)


access_key = "VKLsGkG1ak7K5m1xJEJtUov7buuBpf6kn8_QD3pSsaQ"

word = st.text_input("Enter something to search (like car, nature, laptop)")
btn = st.button("Search")

if btn and word:
    url = f"https://api.unsplash.com/search/photos?query={word}&per_page=8&client_id={access_key}"
    res = requests.get(url).json()

    if "results" in res and res["results"]:
        col1, col2 = st.columns(2)
        for i, photo in enumerate(res["results"]):
            img_url = photo["urls"]["regular"]
            img_data = requests.get(img_url).content
            name = photo["alt_description"] or "unsplash_image"

            if i % 2 == 0:
                with col1:
                    st.image(img_url, caption=name)
                    st.download_button("Download Image", data=img_data, file_name=f"{name}.jpg", mime="image/jpeg")
            else:
                with col2:
                    st.image(img_url, caption=name)
                    st.download_button("Download Image", data=img_data, file_name=f"{name}.jpg", mime="image/jpeg")
    else:
        st.warning("No images found or limit reached.")


st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 16px;'>
        Made with ❤️ by Sarthak Jain <br>
         |Mini Project | Streamlit + Unsplash
    </div>
    """,
    unsafe_allow_html=True
)


