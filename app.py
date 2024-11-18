import streamlit as st

# 在 session_state 中初始化显示状态
if "sidebar_visible" not in st.session_state:
    st.session_state.sidebar_visible = True

# 控制侧边栏显示和隐藏的按钮
if st.button("Toggle Sidebar"):
    st.session_state.sidebar_visible = not st.session_state.sidebar_visible

# 动态渲染侧边栏
if st.session_state.sidebar_visible:
    with st.sidebar:
        st.title("📊 Navigation")
        selected_slide = st.radio("Choose a slide", ["Slide 1", "Slide 2", "Slide 3"])
else:
    st.sidebar.empty()  # 隐藏侧边栏内容

# 主内容区域
st.title(f"Main Content: {selected_slide}")
st.write(f"This is the content of {selected_slide}.")

