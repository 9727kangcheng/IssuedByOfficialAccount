# -*- coding: utf-8 -*-
"""
硬石户外 - 公众号发布技能
自动生成文案、标题、排版、上传素材、推送到草稿箱
"""

import requests
import json
import time
from datetime import datetime

class WechatPublisher:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.token_expires_at = 0
        
    def get_access_token(self):
        """获取微信 access_token"""
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token
            
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_id,
            "secret": self.app_secret
        }
        
        try:
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            
            if "access_token" in data:
                self.access_token = data["access_token"]
                self.token_expires_at = time.time() + data.get("expires_in", 7200) - 300
                print("[OK] Access token obtained")
                return self.access_token
            else:
                print("[ERROR] Failed to get access token:", data.get("errmsg"))
                return None
        except Exception as e:
            print("[ERROR] Network error:", str(e))
            return None
    
    def upload_media(self, file_path, media_type="image"):
        """上传素材到微信"""
        token = self.get_access_token()
        if not token:
            return None
            
        url = "https://api.weixin.qq.com/cgi-bin/media/upload"
        params = {
            "access_token": token,
            "type": media_type
        }
        
        try:
            with open(file_path, 'rb') as f:
                files = {'media': f}
                resp = requests.post(url, params=params, files=files, timeout=30)
                data = resp.json()
                
                if "media_id" in data:
                    print("[OK] Media uploaded, media_id:", data["media_id"])
                    return data["media_id"]
                else:
                    print("[ERROR] Upload failed:", data.get("errmsg"))
                    return None
        except Exception as e:
            print("[ERROR] Upload error:", str(e))
            return None
    
    def create_draft(self, title, content, cover_media_id, video_media_id=None):
        """创建图文草稿"""
        token = self.get_access_token()
        if not token:
            return None
            
        url = "https://api.weixin.qq.com/cgi-bin/draft/add"
        
        # 构建图文消息
        articles = [{
            "title": title,
            "author": "硬石户外",
            "digest": content[:50] + "...",  # 摘要
            "show_cover_pic": 1,
            "content": content,
            "content_source_url": "",
            "thumb_media_id": cover_media_id
        }]
        
        payload = {
            "articles": articles
        }
        
        try:
            resp = requests.post(
                url,
                params={"access_token": token},
                json=payload,
                timeout=10
            )
            data = resp.json()
            
            if "media_id" in data:
                print("[OK] Draft created, media_id:", data["media_id"])
                return data["media_id"]
            else:
                print("[ERROR] Draft creation failed:", data.get("errmsg"))
                return None
        except Exception as e:
            print("[ERROR] Draft error:", str(e))
            return None

def generate_copywriting(location):
    """根据地点生成文案"""
    
    # 地点特色描写库
    location_features = {
        "京西翡翠湖": {
            "intro": "不愧是'京郊小九寨'",
            "feature": "昔日的汉白玉矿坑，如今化作一汪绝美的碧水",
            "scenery": "湖水在光影中变幻着迷人的翠绿色调，清透如宝石",
            "landmark": "千年玉皇塔",
            "terrain": "洁白的汉白玉崖壁"
        }
    }
    
    # 获取地点特色（如果没有，使用通用描写）
    features = location_features.get(location, {
        "intro": "这片山野",
        "feature": "自然风光秀美",
        "scenery": "山水相映成趣",
        "landmark": "沿途风景",
        "terrain": "山野"
    })
    
    # 生成文案
    content = f"""春风拂过山野，万物渐次复苏，硬石户外的家人们齐聚{location}，赴一场春日之约。这是一场久违的相聚，大家卸下城市的忙碌，在专业领队的带领下，沿着舒缓的小径一路前行。

眼前的{location}，{features['intro']}，{features['feature']}。阳光倾泻而下，{features['scenery']}，清透如宝石，与岸边{features['terrain']}相映成趣，构成了一幅绝美的自然画卷。大家穿梭在春风里，脚步轻快，彼此照应，那份独属于团队的默契与温暖，在山野间悄然流淌。

群友们一路欢声笑语，有人在{features['landmark']}下驻足沉思，有人在湖边定格美好瞬间。春日的生机盎然，配上大家发自内心的笑容，让这片{location}更显动人。感谢每一位靠谱的伙伴，是你们的热情与活力，让这次踏青充满了意义。

这个春天，硬石户外与大家一起，在徒步中拥抱自然，在同行中收获情谊。期待下一次，我们继续携手，奔赴更多山野之美！"""
    
    return content

def generate_title(location):
    """生成标题"""
    titles = {
        "京西翡翠湖": "「京西翡翠湖｜春日之约，与你同行」"
    }
    return titles.get(location, f"「{location}｜春日踏青，拥抱自然」")

# 主程序
if __name__ == "__main__":
    # 配置
    APP_ID = "wx668d7edefc166605"
    APP_SECRET = "5e34e46f3d5f79a69ffd5978d88eb826"
    LOCATION = "京西翡翠湖"
    COVER_PATH = r"C:\Users\18320\Desktop\cover.jpg"
    VIDEO_PATH = r"C:\Users\18320\Desktop\1.mp4"
    
    print("=" * 50)
    print("硬石户外 - 公众号发布工作流")
    print("=" * 50)
    print()
    
    # 1. 生成文案和标题
    print("[1/4] 生成文案和标题...")
    title = generate_title(LOCATION)
    content = generate_copywriting(LOCATION)
    print("[OK] Title:", title)
    print("[OK] Content length:", len(content), "characters")
    print()
    
    # 2. 初始化发布器
    print("[2/4] 初始化微信发布器...")
    publisher = WechatPublisher(APP_ID, APP_SECRET)
    print()
    
    # 3. 上传素材
    print("[3/4] 上传素材...")
    cover_media_id = publisher.upload_media(COVER_PATH, "image")
    if not cover_media_id:
        print("[ERROR] Failed to upload cover")
        exit(1)
    print()
    
    # 4. 创建草稿
    print("[4/4] 创建图文草稿...")
    draft_id = publisher.create_draft(title, content, cover_media_id, VIDEO_PATH)
    if draft_id:
        print()
        print("=" * 50)
        print("SUCCESS! 草稿已推送到公众号后台")
        print("=" * 50)
        print("标题:", title)
        print("地点:", LOCATION)
        print("草稿 ID:", draft_id)
        print()
        print("下一步: 登录公众号后台 → 草稿箱 → 预览 → 发布")
    else:
        print("[ERROR] Failed to create draft")
        exit(1)
