import streamlit as st

# 页面基础配置
st.set_page_config(page_title="个人简历生成器", page_icon="📝", layout="wide")
st.title("个人简历生成器")
st.caption("使用Streamlit创建您的个性化简历")

# 分割为左右两列，比例与参考页匹配
col_form, col_preview = st.columns([1, 2], gap="medium")

# ---------------------- 左侧：个人信息表单 ----------------------
with col_form:
    st.subheader("个人信息表单")
    # 基础信息
    name = st.text_input("姓名", placeholder="请输入姓名")
    position = st.text_input("职位", placeholder="请输入应聘职位")
    phone = st.text_input("电话", placeholder="请输入联系电话")
    email = st.text_input("邮箱", placeholder="请输入电子邮箱")
    birthday = st.date_input("出生日期", format="YYYY/MM/DD")
    
    # 性别（改为横向显示）、学历
    gender = st.radio("性别", ["男", "女", "其他"], horizontal=True)  # 核心修改：horizontal=True
    education = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士"], index=0)
    
    # 语言能力、工作经验、期望薪资
    language = st.selectbox("语言能力", ["无", "英语四级", "英语六级", "雅思6.5+", "托福90+"], index=0)
    work_exp = st.slider("工作经验（年）", 0, 30, 0)
    salary = st.slider("期望薪资（元）", 10000, 50000, (10000, 20000))
    contact_time = st.time_input("最佳联系时间")
    
    # 个人简介
    intro = st.text_area("个人简介", placeholder="这个人很神秘，没有留下任何介绍...", height=100)

# ---------------------- 右侧：简历实时预览 ----------------------
with col_preview:
    st.subheader("简历实时预览")
    st.divider()  # 蓝色分割线，匹配参考页样式
    
    # 姓名和核心信息行（左右分栏展示）
    preview_col1, preview_col2 = st.columns([2, 1])
    with preview_col1:
        st.title(name if name else "未填写姓名")
        st.write(f"**职位**：{position if position else '未填写'}")
        st.write(f"**电话**：{phone if phone else '未填写'}")
        st.write(f"**邮箱**：{email if email else '未填写'}")
        st.write(f"**出生日期**：{birthday}")
    
    with preview_col2:
        st.write(f"**性别**：{gender}")
        st.write(f"**学历**：{education}")
        st.write(f"**工作经验**：{work_exp}年")
        st.write(f"**期望薪资**：{salary[0]}-{salary[1]}元")
        st.write(f"**最佳联系时间**：{contact_time}")
        st.write(f"**语言能力**：{language}")
    
    # 个人简介模块
    st.subheader("个人简介")
    st.write(intro if intro else "这个人很神秘，没有留下任何介绍...")
    
