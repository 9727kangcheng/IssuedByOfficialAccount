# -*- coding: utf-8 -*-
"""
硬石户外 - 公众号发布技能演示
展示文案生成、标题生成、排版效果
"""

import sys
import os
import io

# 设置 stdout 编码为 UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 添加技能目录到 Python 路径
skill_dir = r"D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher"
sys.path.insert(0, skill_dir)

from wechat_publisher import generate_copywriting, generate_title

def demo():
    print("=" * 70)
    print("硬石户外 - 微信公众号发布技能演示")
    print("=" * 70)
    print()
    
    # 演示地点
    location = "京西翡翠湖"
    
    # 生成标题
    print("[TITLE]")
    print("-" * 70)
    title = generate_title(location)
    print(title)
    print()
    
    # 生成文案
    print("[CONTENT]")
    print("-" * 70)
    content = generate_copywriting(location)
    print(content)
    print()
    
    # 统计信息
    print("[STATS]")
    print("-" * 70)
    print("Title: " + title)
    print("Characters: " + str(len(content)))
    print("Paragraphs: " + str(len(content.split('\n\n'))))
    print()
    
    # 排版预览
    print("[PREVIEW]")
    print("-" * 70)
    print()
    print("[" + location + "]")
    print()
    print(title)
    print()
    print("[Cover Image]")
    print()
    print(content)
    print()
    print("-" * 70)
    print()
    
    print("[SUCCESS] Demo completed!")
    print()
    print("Next steps:")
    print("1. Configure IP whitelist in WeChat Official Account backend")
    print("2. Provide location + image/video file")
    print("3. Skill will auto-push to drafts")
    print()

if __name__ == "__main__":
    demo()
