import streamlit as st

# 创建目录
menu = [
    ("Streamlit 简介", [
        "什么是 Streamlit？", 
        "Streamlit 的基本特点", 
        "如何安装和使用 Streamlit"
    ]),
    ("Streamlit 基本组件", [
        "`st.title()`：标题", "`st.write()`：文本输出", "`st.text()`、`st.markdown()`：不同格式的文本",
        "`st.button()`：按钮", "`st.checkbox()`：复选框", "`st.radio()`：单选框", "`st.selectbox()`：下拉框",
        "`st.text_input()` 和 `st.number_input()`：用户输入"]),
    ("布局和布局管理", [
        "使用 `st.sidebar` 创建侧边栏", 
        "使用 `st.columns()` 创建多列布局", 
        "控制页面元素布局：`st.empty()` 和动态布局"]),
    ("数据可视化", [
        "使用 `st.line_chart()` 和 `st.bar_chart()` 绰图", 
        "使用 `st.pyplot()` 显示 Matplotlib 图形",
        "使用 `st.altair_chart()` 或 `st.plotly_chart()` 显示交互式图表"]),
    ("交互式组件", [
        "使用 `st.slider()` 创建滑块", 
        "使用 `st.date_input()` 和 `st.time_input()` 获取日期和时间", 
        "创建表单：`st.form()`"]),
    ("处理文件和上传文件", [
        "使用 `st.file_uploader()` 上传文件", 
        "处理上传的图片、文本文件、CSV 文件等"]),
    ("状态管理和会话", [
        "使用 `st.session_state` 保持用户的选择和状态", 
        "使用 `st.cache()` 缓存数据以提高性能"]),
    ("应用布局和主题", [
        "自定义页面的主题、布局和颜色", 
        "使用 `st.set_page_config()` 设置页面配置"]),
    ("部署 Streamlit 应用", [
        "如何将 Streamlit 应用部署到 Streamlit Cloud", 
        "部署到其他云平台：Heroku、AWS、GCP"]),
    ("进阶功能和技巧", [
        "与其他库（如 Pandas、Scikit-learn）结合使用", 
        "使用 `st.experimental` 尝试实验性功能", 
        "集成机器学习模型和实时数据更新"]),
    ("实例应用：幻灯片展示", [
        "用 Streamlit 实现简单的幻灯片展示功能", 
        "使用侧边栏导航切换幻灯片内容", 
        "动态更新图表和数据表"]),
    ("常见问题与调试", [
        "解决 Streamlit 常见错误", 
        "调试技巧与日志记录"])
]

# 侧边栏目录
with st.sidebar:
    st.title("教学目录")

    # 遍历每个章节，使用 `st.expander` 使每个章节小标题可展开
    for section, content in menu:
        with st.expander(section):
            # 展开后显示该章节的内容
            for item in content:
                st.write(item)
