# -*- coding: utf-8 -*-
import requests, json, os

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

# 获取 token
token = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10).json()['access_token']
print('Token OK')

# 上传图片
img_path = r'C:\Users\18320\.qclaw\media\inbound\444478a9-d403-476c-8c2c-f8b0c7e8b793.jpg'
with open(img_path, 'rb') as f:
    upload_resp = requests.post(
        'https://api.weixin.qq.com/cgi-bin/material/add_material',
        params={'access_token': token, 'type': 'image'},
        files={'media': ('cover.jpg', f, 'image/jpeg')},
        timeout=30
    )
upload_data = upload_resp.json()
print('Upload:', json.dumps(upload_data, ensure_ascii=False))
thumb_media_id = upload_data['media_id']
img_url = upload_data['url']

# 标题
title = '居庸关｜穿越千年，看万里长城的壮阔波澜'

# 文案（自由创作风格）
intro = (
    '居庸关，被称为"天下第一雄关"，'
    '扼守着京城北大门的重要通道。'
    '春日里的居庸关，少了凛冽的寒风，多了几分温柔与从容。'
)
feature = (
    '山峦起伏间，古老的城墙蜿蜒伸展，'
    '敌楼、烽火台静静伫立，仿佛在诉说千年的沧桑。'
)
scene1 = (
    '阳光穿过城墙垛口洒落下来，'
    '在青石台阶上投下斑驳的光影。'
    '脚下是厚重的历史，远处是连绵的山脉，'
    '那种站在天地之间的感觉，只有真正来过才能体会。'
)
scene2 = (
    '队员们三两结伴，边走边聊，'
    '笑声在山谷间回荡。'
    '有人说，走过居庸关，才算真正感受到了北京的脊梁。'
    '是啊，这座城关，见证过多少金戈铁马，'
    '如今又迎来一群热爱山野的户外人，赋予它新的活力。'
)
ending = (
    '每一步攀登，都是与历史的对话。'
    '感谢硬石户外的每一位同行者，'
    '是你们的脚步，让这段长城故事有了新的续写。'
    '下一站，等你来。'
)

# 排版：第一段文案 → 图片 → 剩余文案
content = (
    '<p>' + intro + '</p>'
    '<p style="text-align:center"><img src="' + img_url + '" style="max-width:100%"/></p>'
    '<p>' + feature + '</p>'
    '<p>' + scene1 + '</p>'
    '<p>' + scene2 + '</p>'
    '<p>' + ending + '</p>'
)

draft_data = {
    'articles': [{
        'title': title,
        'author': '',
        'digest': '居庸关的春日徒步，与硬石户外一起穿越千年，感受万里长城的壮阔与温柔。',
        'content': content,
        'content_source_url': '',
        'thumb_media_id': thumb_media_id,
        'show_cover_pic': 1,
        'need_open_comment': 1,
        'only_fans_can_comment': 0
    }]
}

resp = requests.post(
    'https://api.weixin.qq.com/cgi-bin/draft/add',
    params={'access_token': token},
    data=json.dumps(draft_data, ensure_ascii=False).encode('utf-8'),
    headers={'Content-Type': 'application/json; charset=utf-8'},
    timeout=15
)
result = resp.json()
print('Draft:', json.dumps(result, ensure_ascii=False))
