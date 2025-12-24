import streamlit as st

# 1. 先定义视频数组，确保后续代码能调用
video_arr = [
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/19/69/756226919/756226919-1-208.mp4?e=ig8euxZM2rNcNbh17wdVhwdlhzRMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&nbs=1&platform=html5&oi=771356656&trid=249adde5a173469f901b3c4dbfdf548h&os=cosovbv&og=hw&deadline=1766567321&uipk=5&gen=playurlv3&upsig=997456976fbb387a13d64753840ee84a&uparams=e,mid,nbs,platform,oi,trid,os,og,deadline,uipk,gen&bvc=vod&nettype=0&bw=2513983&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title': '《怪奇物语》第一季解说'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/78/47/756244778/756244778-1-208.mp4?e=ig8euxZM2rNcNbh17WdVhwdlhzRBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=07138d0214544ee7855f5b465c50f1ch&nbs=1&uipk=5&oi=771356656&mid=0&deadline=1766567532&os=cosovbv&platform=html5&gen=playurlv3&og=cos&upsig=dd2f79a7f965dd1cd743ec6db713bb8f&uparams=e,trid,nbs,uipk,oi,mid,deadline,os,platform,gen,og&bvc=vod&nettype=0&bw=2520165&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
        'title': '《怪奇物语》第二季解说'
    },
    {
        'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/37/73/758057337/758057337-1-208.mp4?e=ig8euxZM2rNcNbhMhwdVhwdlhzKVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766567565&nbs=1&uipk=5&oi=771356656&os=cosovbv&platform=html5&trid=f61ca2d390ba4fd58cb10a343c8d965h&gen=playurlv3&og=hw&mid=0&upsig=6c5c8909d5267a6524ab85bbeb268747&uparams=e,deadline,nbs,uipk,oi,os,platform,trid,gen,og,mid&bvc=vod&nettype=0&bw=2723258&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
        'title': '《怪奇物语》第三季解说'
    }
]

# 2. 初始化session_state
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 3. 页面配置与标题（此时video_arr已定义，可正常调用）
st.set_page_config(page_title="视频中心")
st.title(video_arr[st.session_state['ind']]['title'])

# 4. 播放视频
st.video(video_arr[st.session_state['ind']]['url'])

# 5. 定义切换视频的函数
def playVideo(e):
    st.session_state['ind'] = int(e)

# 6. 选集按钮
st.write("**选集**")
cols = st.columns(3)

# 7. 生成横向集数按钮（核心修改部分）
cols = st.columns(len(video_arr))  # 创建与视频数量匹配的列
for i, col in enumerate(cols):
    with col:
        # 根据视频标题提取季数，让按钮更贴合内容
        season = video_arr[i]['title'].split('第')[1].split('季')[0]
        st.button(f'第{season}季', on_click=playVideo, args=(i,))
