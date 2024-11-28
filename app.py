import streamlit as st

# 模拟的菜单结构：章节 -> 大标题 -> 小标题 -> 具体内容
menu = {
    "简介": {
        "程序目的": {
            "目标": "教会学生机器学习，以及使用 Streamlit 来做一个自己的机器学习小程序",
            "方法": "通过实际操作和例子，帮助学生掌握机器学习的基本概念。"
        },
        "关于我": {
            "个人介绍": "我是 Shuying-exquisite，一名热衷于研究机器学习和编程的开发者。",
            "工作经历": "目前在某科技公司担任数据科学家，致力于机器学习应用和研究。"
        },
        "我的 GitHub": {
            "GitHub 主页": "[点击这里访问我的 GitHub](https://github.com/Shuying-exquisite)"
        }
    },
    "第一章：机器学习基础": {
        "机器学习西瓜书": {
            "概述": "机器学习基础部分具体参考周老师的西瓜书。",
            "学习内容": "从基础的机器学习概念到经典算法的实现和应用。"
        },
        "st.write()：文本输出": {
            "功能介绍": "st.write() 是一个万能的输出函数，可以输出文本、表格、图形等。",
            "使用方法": "使用 `st.write()` 来显示任何类型的内容。"
        },
        "st.button()：按钮": {
            "功能介绍": "st.button('按钮') 创建一个按钮组件，用户点击后触发事件。",
            "使用方法": "通过按钮与用户交互，执行特定的代码。"
        }
    }
}

# 侧边栏目录
with st.sidebar:
    st.title("目录")
    
    # 选择章节
    selected_section = st.selectbox("选择章节:", list(menu.keys()))

    # 选择大标题
    selected_main_title = st.selectbox("选择大标题:", list(menu[selected_section].keys()))

    # 选择小标题
    selected_sub_title = st.selectbox("选择小标题:", list(menu[selected_section][selected_main_title].keys()))

# 根据选择的小标题在主界面展示内容
if selected_section:
    st.title(selected_section)
    st.subheader(selected_main_title)
    st.write(f"**{selected_sub_title}:** {menu[selected_section][selected_main_title][selected_sub_title]}")
