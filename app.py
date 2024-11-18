import streamlit as st

# 初始化页面状态
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

# 定义幻灯片内容
slides = [
    {"title": "Slide 1: Introduction", "content": "Welcome to the first slide!"},
    {"title": "Slide 2: Analysis", "content": "Here is some analysis."},
    {"title": "Slide 3: Conclusion", "content": "Thank you for viewing this presentation!"},
]

# 侧边栏导航
with st.sidebar:
    st.title("Navigation")
    page_options = [f"Slide {i+1}" for i in range(len(slides))]
    selected_page = st.radio("Go to Slide", page_options)
    st.write("---")
    if st.button("Next") and st.session_state.current_slide < len(slides) - 1:
        st.session_state.current_slide += 1
    if st.button("Previous") and st.session_state.current_slide > 0:
        st.session_state.current_slide -= 1

# 更新页面状态
st.session_state.current_slide = page_options.index(selected_page)

# 渲染当前幻灯片
current_slide = slides[st.session_state.current_slide]
st.title(current_slide["title"])
st.write(current_slide["content"])
