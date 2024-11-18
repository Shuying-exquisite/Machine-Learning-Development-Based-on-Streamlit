import streamlit as st

# 创建目录
menu = {
    "Streamlit 简介": [
        ("什么是 Streamlit？", "Streamlit 是一个快速构建 Web 应用的框架，可以通过简单的 Python 代码生成交互式界面。"),
        ("Streamlit 的基本特点", "Streamlit 提供了丰富的组件，如文本、按钮、图表等，可以方便地进行数据展示和交互。"),
        ("如何安装和使用 Streamlit", "通过 `pip install streamlit` 安装 Streamlit，使用 `streamlit run` 启动应用。")
    ],
    "Streamlit 基本组件": [
        ("`st.title()`：标题", "`st.title('标题')` 用来设置网页的主标题。"),
        ("`st.write()`：文本输出", "`st.write()` 是一个万能的输出函数，可以输出文本、表格、图形等。"),
        ("`st.button()`：按钮", "`st.button('按钮')` 创建一个按钮组件，用户点击后触发事件。")
    ],
    # 其他章节...
}

# 侧边栏目录
with st.sidebar:
    st.title("教学目录")
    
    # 选择章节
    selected_section = st.selectbox("选择章节:", list(menu.keys()))
    
    # 展开章节的小标题
    selected_topic = st.radio("选择小标题:", [item[0] for item in menu[selected_section]])

# 根据选择的小标题展示内容
if selected_section:
    st.title(selected_section)
    for title, content in menu[selected_section]:
        if title == selected_topic:
            st.subheader(title)
            
            # 如果内容很长，进行分页显示
            content_parts = content.split("\n")  # 假设每个段落用换行符分隔
            num_parts = len(content_parts)
            part_size = 5  # 每页显示 5 个段落
            total_pages = (num_parts // part_size) + (1 if num_parts % part_size > 0 else 0)
            
            page = st.slider("选择页面:", 1, total_pages, 1)  # 页面选择滑块
            start_index = (page - 1) * part_size
            end_index = start_index + part_size
            
            for part in content_parts[start_index:end_index]:
                st.write(part)
            
            # 如果内容未完，可以显示继续按钮
            if page < total_pages:
                if st.button("下一页"):
                    st.experimental_rerun()  # 刷新以显示下一页
