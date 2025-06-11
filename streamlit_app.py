import streamlit as st

st.set_page_config(page_title="FutureFound App", page_icon="🚀")

st.markdown("""
    <style>
    /* Erzwinge dein aktuelles Theme auf allen Geräten */
    .stApp {
        background-color: #23272f !important;
        color: #ffffff !important;
    }
    
    /* Überschreibe System-Theme-Preferences */
    @media (prefers-color-scheme: light), (prefers-color-scheme: dark) {
        .stApp {
            background-color: #23272f !important;
            color: #ffffff !important;
        }
    }
    
    /* Mobile-spezifische Absicherung */
    @media only screen and (max-width: 768px) {
        .stApp {
            background-color: #23272f !important;
            color: #ffffff !important;
        }
    }

/* Button-Text und Hintergrund überall erzwingen */
.stButton > button {
    background-color: #393e46 !important;
    color: #fff !important;
    border: 2px solid #00adb5 !important;
    font-weight: 500 !important;
    font-size: 1em !important;
    border-radius: 8px !important;
    text-shadow: none !important;
    -webkit-appearance: none !important;
    -moz-appearance: none !important;
    appearance: none !important;
}

/* Mobile: Button-Styles noch einmal explizit überschreiben */
@media only screen and (max-width: 768px) {
    .stButton > button {
        background-color: #393e46 !important;
        color: #fff !important;
        border: 2px solid #00adb5 !important;
        font-weight: 600 !important;
        font-size: 1.1em !important;
        border-radius: 8px !important;
        text-shadow: none !important;
        -webkit-appearance: none !important;
        -moz-appearance: none !important;
        appearance: none !important;
    }
}
    
    </style>
""", unsafe_allow_html=True)


# Seite 1
st.title("Willkommen!")
st.write("""
Du bist Business Consultant, Spezialistin für smarte Startups (also, fast… jedenfalls behauptet das dein LinkedIn-Profil).
Eines Tages bekommst du eine Nachricht vom kleinen, innovativen Startup FutureFound, das kurz vor dem Aus steht.
""")
video_file = open("video 1.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

if st.button("Mission starten!"):
    st.switch_page("pages/2_Kapitel 1.py")
