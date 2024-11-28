import streamlit as st
import base64
import os
import time  # 用于模拟加载延迟，实际开发中可以去掉

# 创建目录
menu = {
    "简介": [
        ("我做这个程序的目的", "教会学生机器学习，以及使用 Streamlit 来做一个自己的机器学习小程序 "),
        ("关于我", "我是 Shuying-exquisite，一名热衷于研究机器学习和编程的开发者；我希望通过我的教学，能够让更多人理解机器学习，并能够在各自的领域内应用这些技术。"),
        ("我的 GitHub", "[点击这里访问我的 GitHub](https://github.com/Shuying-exquisite)"),
    ],
    "第一章：机器学习基础": [
        ("机器学习西瓜书", "机器学习基础部分具体参考周老师的西瓜书。"),
        ("st.write()：文本输出", "st.write() 是一个万能的输出函数，可以输出文本、表格、图形等。"),
        ("st.button()：按钮", "st.button('按钮') 创建一个按钮组件，用户点击后触发事件。"),
    ],
    "第二章：布局和布局管理": [
        ("使用 st.sidebar 创建侧边栏", "通过 st.sidebar 可以创建侧边栏，用来放置控件或内容。"),
        ("使用 st.columns() 创建多列布局", "通过 st.columns() 可以创建多个并排的列，布局更加灵活。"),
        ("控制页面元素布局：st.empty() 和动态布局", "st.empty() 可以动态调整页面元素的位置。"),
    ],
    "第三章：交互功能": [
        ("使用 st.button() 处理按钮事件", "按钮组件用于触发用户交互事件，可以根据用户点击按钮的状态执行不同的代码。"),
        ("使用 st.slider() 获取用户输入", "st.slider() 允许用户通过滑块选择一个范围，适用于获取数字类型的输入。"),
        ("使用 st.selectbox() 获取单项选择", "通过 st.selectbox()，用户可以选择下拉框中的一个选项，适用于单项选择。"),
    ],
    "第四章：数据展示与可视化": [
        ("使用 st.line_chart() 绘制折线图", "通过 st.line_chart() 可以非常方便地绘制折线图，展示趋势变化。"),
        ("使用 st.bar_chart() 绘制柱状图", "通过 st.bar_chart() 可以绘制柱状图，展示各类数据的比较。"),
        ("使用 st.map() 展示地图", "通过 st.map() 可以直接在页面中显示地理位置数据，绘制地图。"),
    ],
    "第五章：高级功能与优化": [
        ("使用 st.cache() 优化性能", "通过 st.cache() 可以缓存计算结果，避免重复计算，提高程序性能。"),
        ("使用 st.file_uploader() 上传文件", "st.file_uploader() 允许用户上传文件，可以处理各种类型的文件输入。"),
        ("使用 st.text_area() 输入多行文本", "通过 st.text_area() 可以让用户输入多行文本，适用于较长内容的输入。"),
    ]
}

# 侧边栏目录
with st.sidebar:
    st.title("目录")
    
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

            # 如果选择了 "机器学习西瓜书"，则提供 PDF 查看功能
            if title == "机器学习西瓜书":
                # 假设 PDF 文件在同一个文件夹中
                pdf_file_path = "机器学习 Machine Learning (Chinese Edition) (Zhou Zhihua 周志华) .pdf"  # 请确保文件名与实际文件匹配

                if os.path.exists(pdf_file_path):
                    # 显示加载提示
                    with st.spinner('正在加载 PDF，请稍等...'):
                        time.sleep(2)  # 用于模拟加载延迟，实际开发中可以去掉这个延迟

                        # 将 PDF 文件转换为 base64 编码
                        with open(pdf_file_path, "rb") as pdf_file:
                            pdf_data = pdf_file.read()
                        pdf_base64 = base64.b64encode(pdf_data).decode("utf-8")

                        # 创建嵌入的 PDF URL
                        pdf_url = f"data:application/pdf;base64,{pdf_base64}"

                        # 使用 iframe 嵌入 PDF 文件
                        st.markdown(f"""
                            <iframe src="{pdf_url}" width="700" height="800" type="application/pdf"></iframe>
                        """, unsafe_allow_html=True)

                else:
                    st.error("找不到 PDF 文件，请确保文件存在并且路径正确。")
