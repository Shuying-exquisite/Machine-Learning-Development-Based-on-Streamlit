import streamlit as st

# 定义当前页面状态
if "page" not in st.session_state:
    st.session_state.page = 0

# 创建页面内容
def show_page(page):
    if page == 0:
        st.title("Slide 1: Introduction")
        st.write("Welcome to the first slide!")
    elif page == 1:
        st.title("Slide 2: Analysis")
        st.write("This is the analysis slide.")
    elif page == 2:
        st.title("Slide 3: Conclusion")
        st.write("Thanks for reviewing this presentation.")

# 显示当前页面
show_page(st.session_state.page)

# 创建导航按钮
col1, col2, col3 = st.columns([1, 2, 1])
if col1.button("Previous") and st.session_state.page > 0:
    st.session_state.page -= 1
if col3.button("Next") and st.session_state.page < 2:
    st.session_state.page += 1
