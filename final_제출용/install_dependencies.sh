#!/bin/bash

echo "필요한 Python 패키지들을 설치합니다..."

# pip 업그레이드
python -m pip install --upgrade pip

# 필요한 패키지 설치
pip install selenium==4.18.1
pip install beautifulsoup4==4.12.3
pip install requests==2.31.0
pip install webdriver-manager==4.0.1

echo "설치가 완료되었습니다."
echo "Chrome 브라우저가 설치되어 있는지 확인해주세요." 