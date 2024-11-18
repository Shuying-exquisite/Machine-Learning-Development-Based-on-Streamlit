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
    "布局和布局管理": [
        ("使用 `st.sidebar` 创建侧边栏", "通过 `st.sidebar` 可以创建侧边栏，用来放置控件或内容。"),
        ("使用 `st.columns()` 创建多列布局", "通过 `st.columns()` 可以创建多个并排的列，布局更加灵活。"),
        ("控制页面元素布局：`st.empty()` 和动态布局", "`st.empty()` 可以动态调整页面元素的位置。")
    ],
    "交互功能": [
        ("使用 `st.button()` 处理按钮事件", "按钮组件用于触发用户交互事件，可以根据用户点击按钮的状态执行不同的代码。"),
        ("使用 `st.slider()` 获取用户输入", "`st.slider()` 允许用户通过滑块选择一个范围，适用于获取数字类型的输入。"),
        ("使用 `st.selectbox()` 获取单项选择", "通过 `st.selectbox()`，用户可以选择下拉框中的一个选项，适用于单项选择。")
    ],
    "数据展示与可视化": [
        ("使用 `st.line_chart()` 绘制折线图", "通过 `st.line_chart()` 可以非常方便地绘制折线图，展示趋势变化。"),
        ("使用 `st.bar_chart()` 绘制柱状图", "通过 `st.bar_chart()` 可以绘制柱状图，展示各类数据的比较。"),
        ("使用 `st.map()` 展示地图", "通过 `st.map()` 可以直接在页面中显示地理位置数据，绘制地图。")
    ],
    "高级功能与优化": [
        ("使用 `st.cache()` 优化性能", "通过 `st.cache()` 可以缓存计算结果，避免重复计算，提高程序性能。"),
        ("使用 `st.file_uploader()` 上传文件", "`st.file_uploader()` 允许用户上传文件，可以处理各种类型的文件输入。"),
        ("使用 `st.text_area()` 输入多行文本", "通过 `st.text_area()` 可以让用户输入多行文本，适用于较长内容的输入。")
    ]
}

# 侧边栏目录
with st.sidebar:
    st.title("教学目录")
    
    # 选择章节
    selected_section = st.selectbox("选择章节:", list(menu.keys()))
    
    # 展开章节的小标题
    selected_topic = st.radio("选择小标题:", [item[0] for item in menu[selected_section]])

# 根据选择的小标题在主界面展示内容
if selected_section:
    st.title(selected_section)
    # 获取选中的小标题的内容
    for title, content in menu[selected_section]:
        if title == selected_topic:
            st.subheader(title)
            st.write(content)


