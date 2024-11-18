import streamlit as st

# 定义幻灯片内容
slides = [
    {"title": "Slide 1: Introduction", "content": "Welcome to the first slide! Learn about the basics."},
    {"title": "Slide 2: Analysis", "content": "Here is some analysis with charts and data."},
    {"title": "Slide 3: Conclusion", "content": "Thank you for viewing this presentation!"}
]

# 侧边栏显示幻灯片列表
with st.sidebar:
    st.title("📑 Slide Navigator")
    # 显示幻灯片选择器
    slide_titles = [slide["title"] for slide in slides]
    selected_slide_title = st.radio("Choose a Slide:", slide_titles)

# 找到当前选择的幻灯片
selected_slide = None
for slide in slides:
    if slide["title"] == selected_slide_title:
        selected_slide = slide
        break

# 主界面显示当前幻灯片
st.title(selected_slide["title"])
st.write(selected_slide["content"])

# 可以在主内容区添加更多功能，如图表、数据表等
if selected_slide["title"] == "Slide 2: Analysis":
    st.bar_chart({"Category A": [3, 5, 2], "Category B": [6, 7, 8]})
elif selected_slide["title"] == "Slide 3: Conclusion":
    st.write("### Summary of Key Findings")
    st.dataframe({"Feature 1": [1, 2, 3], "Feature 2": [4, 5, 6]})
