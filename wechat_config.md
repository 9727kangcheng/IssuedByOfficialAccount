# 硬石户外 - 微信公众号发布技能配置

## 微信公众号配置
- **AppID**: wx668d7edefc166605
- **AppSecret**: 5e34e46f3d5f79a69ffd5978d88eb826
- **公众号ID**: gh_ca4e8fbf5a65

## ⚠️ 微信API字段限制规则（必须遵守）

| 字段 | 限制 | 示例 |
|------|------|------|
| **标题 title** | ≤64字符 | 春日聚山野，漫步翡翠湖｜硬石户外踏青记（19字符） |
| **作者 author** | ≤20字符 | HardRock硬石户外（8字符）✅ / 硬石户外（5字符）✅ |
| **摘要 digest** | ≤54字符 | 自动截取正文前54字符 |
| **封面 thumb_media_id** | 必须先上传到临时素材库，type=thumb，<64KB | 必需字段 |

## 封面图片规则
- 必须使用 `type=thumb` 的临时素材接口上传
- 文件大小必须 <64KB
- 上传后返回的 media_id 用于创建草稿

## 正文图片规则
- 使用 `uploadimg` 接口上传，返回 URL
- 直接将 URL 插入到 HTML 内容中：`<img src="URL" />`

## 视频规则
- 使用 `material/add_material` 接口上传 type=video
- 需要额外参数：title 和 introduction
- 上传后返回 media_id

## 常用API接口

### 1. 获取 access_token
```
GET https://api.weixin.qq.com/cgi-bin/token
?grant_type=client_credential
&appid=wx668d7edefc166605
&secret=5e34e46f3d5f79a69ffd5978d88eb826
```

### 2. 上传临时素材（封面用）
```
POST https://api.weixin.qq.com/cgi-bin/media/upload
?access_token=xxx
&type=thumb
```

### 3. 上传图文内容中的图片
```
POST https://api.weixin.qq.com/cgi-bin/media/uploadimg
?access_token=xxx
```

### 4. 上传视频素材
```
POST https://api.weixin.qq.com/cgi-bin/material/add_material
?access_token=xxx
&type=video
```

### 5. 创建草稿
```
POST https://api.weixin.qq.com/cgi-bin/draft/add
?access_token=xxx
```

## 发布脚本位置
- 最终版：`C:\Users\18320\Desktop\wechat_publish_final.py`

## 素材文件夹
- 路径：`C:\Users\18320\Desktop\gongzhonghao`
- 内容：
  - cover_5s.jpg（封面，从视频提取）
  - 01c0890b3c41480b53210c197c7e1e4.jpg
  - 110e41f65f7641c0abe9a622eba937d.jpg
  - 32678e968eafe06827938272cec92f0.jpg
  - 53cb88ff6b51ac130dee328cc4c044e.jpg
  - b0c4bb1086462b503ecadf88d669d32.jpg
  - fe21d640458dfc25e479e7034113258.jpg
  - 1.mp4（视频）

## 标题和作者规范
- **标题格式**：「地点｜一句话描述」
- **作者**：HardRock硬石户外

## 常见错误
- 40006: 无效的media_id
- 40007: 缺少thumb_media_id
- invalid media size: 封面图片太大
- title size out of limit: 标题超长
- author size out of limit: 作者名超长
