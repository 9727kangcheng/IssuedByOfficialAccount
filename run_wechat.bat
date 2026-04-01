@echo off
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
cd /d "D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher"
python wechat_publisher.py %*
