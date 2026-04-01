## 公众号发布技能 - 硬石户外 ✅ 已完成

### 基本信息
- **公众号名称**: 硬石户外
- **公众号ID**: gh_ca4e8fbf5a65
- **AppID**: wx668d7edefc166605
- **AppSecret**: 5e34e46f3d5f79a69ffd5978d88eb826

### 核心规则（已固化到主程序）
| 配置项 | 值 | 说明 |
|--------|-----|------|
| **作者** | `HardRock硬石户外` | 固定8字符，显示在文章底部 |
| **标题长度** | ≤10字符（中文） | 微信API硬限制，中文最多10字 |
| **文案风格** | AI自由发挥 | 不使用固定模板 |
| **封面图片** | thumb类型永久素材 | 必须用thumb类型，image类型不行 |

### 技术坑（2026-03-31记录）
- ❌ 微信草稿API的title限制：**中文最多10个字符**（不是64字符！）
- ❌ 封面必须上传为 `thumb` 类型，不能用 `image` 类型
- ❌ `material/add_news` 接口已废弃
- ✅ 最终方案：封面用thumb类型，创建草稿时传thumb_media_id

### 工作流程
1. 用户提供：关键字地点 + 图片/视频
2. 技能生成：文案（按模板改写） + 标题
3. 技能处理：
   - 上传图片/视频到公众号素材库
   - 从视频中提取封面（或用户指定的图片作封面）
   - 排版设计（春日主题风格）
   - 推送到公众号草稿箱
4. 用户操作：在公众号后台预览 → 发布

### 设计风格
- 主题：春日、户外、团队、自然
- 色调：翠绿、清爽、温暖
- 排版：段落清晰、图文穿插、留白舒适
- 标题格式：「地点名｜一句话亮点」

### 技能实现状态 ✅ 已完成
✅ 文案生成引擎（按模板改写）
✅ 标题生成
✅ 视频封面提取（OpenCV）
✅ 微信 API 集成框架
✅ 草稿创建逻辑
✅ 完整文档和使用指南
✅ 演示脚本和测试

### 已处理的地点

#### 京西翡翠湖 ✅
- **处理时间**：2026-03-31 11:45 GMT+8
- **素材文件夹**：C:\Users\18320\Desktop\gongzhonghao\
- **视频**：1.mp4（108.3 MB，89.4 秒，1920x1080）
- **原始图片**：6 张（总计 25.8 MB）
- **提取的封面**：3 张（cover_5s.jpg、cover_10s.jpg、cover_15s.jpg）
- **生成的标题**：「京西翡翠湖｜春日之约，与你同行」
- **生成的文案**：384 字，4 段落，完全按模板改写
- **处理报告**：C:\Users\18320\Desktop\gongzhonghao\PROCESSING_REPORT.md

### 文件位置
- 技能主程序：`D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\wechat_publisher.py`
- 技能说明：`D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\SKILL.md`
- 使用指南：`D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\README.md`
- 配置文件：`D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\config.json`
- 演示脚本：`C:\Users\18320\.qclaw\workspace\demo_wechat_publisher.py`
- 素材文件夹：`C:\Users\18320\Desktop\gongzhonghao\`
- 处理报告：`C:\Users\18320\Desktop\gongzhonghao\PROCESSING_REPORT_REPORT.md`

### ⚠️ 需要配置
- 微信公众号 IP 白名单（在公众号后台配置）
- 当前 IP 地址：117.107.140.138（需要添加到白名单中）

### 使用方式
1. 告诉我地点 + 图片/视频文件路径
2. 技能自动完成全流程
3. 你在公众号后台预览 → 发布

### 下一步
1. 配置 IP 白名单（添加 117.107.140.138）
2. 告诉我"准备好了"
3. 我会自动推送到公众号草稿箱
