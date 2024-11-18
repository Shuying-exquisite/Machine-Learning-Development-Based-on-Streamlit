import streamlit as st

# 初始化页面状态
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

# 定义幻灯片内容
slides = [
    {"title": "Slide 1: Introduction", "content": "Welcome to the first slide! Learn about the basics."},
    {"title": "Slide 2: Analysis", "content": "Here is some analysis with charts and data."},
    {"title": "Slide 3: Conclusion", "content": "Thank you for viewing this presentation!"},
]

# 侧边栏增强
with st.sidebar:
    st.title("📊 Slide Navigator")
    # 显示选择器
    page_options = [f"Slide {i+1}" for i in range(len(slides))]
    selected_page = st.radio("Select a Slide:", page_options)
    
    st.write("---")
    # 添加额外功能，比如跳转按钮
    if st.button("Next Slide") and st.session_state.current_slide < len(slides) - 1:
        st.session_state.current_slide += 1
    if st.button("Previous Slide") and st.session_state.current_slide > 0:
        st.session_state.current_slide -= 1
    
    st.write("---")
    # 在侧边栏添加额外内容
    st.info("💡 **Tips:** Use the buttons or select a slide to navigate.")
    st.markdown("""
    **About the Presentation:**
    - 📘 Covers basics, analysis, and conclusions.
    - 🖼️ Includes charts and visual aids.
    - 🎯 Easy to navigate.
    """)

# 更新当前页面状态
st.session_state.current_slide = page_options.index(selected_page)

# 渲染当前幻灯片内容
current_slide = slides[st.session_state.current_slide]
st.title(current_slide["title"])
st.write(current_slide["content"])

# 示例内容：在每张幻灯片展示额外内容
if st.session_state.current_slide == 1:
    st.bar_chart({"Category A": [3, 5, 2], "Category B": [6, 7, 8]})
elif st.session_state.current_slide == 2:
    st.write("### Data Table Example")
    st.dataframe({"Feature 1": [1, 2, 3], "Feature 2": [4, 5, 6]})

