import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Caiden Kopcik"
PROGRAM = "CS39 AE / Computer Science / Role"
INTRO = (
    "I'm a full-stack developer and a computer science student currently learning about "
    "data visualization and human-centered design. I enjoy creating interactive visualizations "
    "that communicate meaningful patterns and stories through data."
)
FUN_FACTS = [
    "I love Playing video games in my spare time.",
    "I’m learning to better my coding abilies through various assinments/projects.",
    "I want to build either an app and successful website that helps people in anyway possible (lifestyle wise).",
]
PHOTO_PATH = "IMG_2159.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
