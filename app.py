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

# 使用st.columns来模拟两个侧边栏
col1, col2 = st.columns([1, 3])  # 1: 侧边栏1, 3: 主内容区域

# 侧边栏1 - 页面导航
with col1:
    st.title("📊 Navigation")
    page_options = [f"Slide {i+1}" for i in range(len(slides))]
    selected_page = st.radio("Select a Slide:", page_options)

    st.write("---")
    if st.button("Next Slide") and st.session_state.current_slide < len(slides) - 1:
        st.session_state.current_slide += 1
    if st.button("Previous Slide") and st.session_state.current_slide > 0:
        st.session_state.current_slide -= 1

# 侧边栏2 - 工具或设置
with col2:
    st.title("⚙️ Settings")
    st.write("Here you can adjust the settings or use tools.")
    setting_option = st.radio("Choose a Tool:", ["Tool 1", "Tool 2", "Tool 3"])
    st.write(f"You selected {setting_option}.")
    
    st.write("---")
    st.info("💡 **Tips:** You can switch between tools as needed.")
    
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

