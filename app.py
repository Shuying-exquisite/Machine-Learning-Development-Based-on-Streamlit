import streamlit as st

# 定义幻灯片内容
slides = [
    {"title": "幻灯片 1: 介绍", "content": "欢迎来到第一张幻灯片！了解基础知识。"},
    {"title": "幻灯片 2: 分析", "content": "这是一些带有图表和数据的分析。"},
    {"title": "幻灯片 3: 结论", "content": "感谢您查看这次演示！"}
]

# 侧边栏显示幻灯片列表
with st.sidebar:
    st.title("📑 幻灯片导航")
    # 显示幻灯片选择器
    slide_titles = [slide["title"] for slide in slides]
    selected_slide_title = st.radio("选择幻灯片:", slide_titles)

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
if selected_slide["title"] == "幻灯片 2: 分析":
    st.bar_chart({"类别 A": [3, 5, 2], "类别 B": [6, 7, 8]})
elif selected_slide["title"] == "幻灯片 3: 结论":
    st.write("### 关键发现总结")
    st.dataframe({"特征 1": [1, 2, 3], "特征 2": [4, 5, 6]})
