# KREAM 상품 모니터링 시스템
에너지응용프로그래밍
Tue,Thu 10:00-01:00
Fri 11:00-12:00
이 프로젝트는 KREAM 사이트의 특정 상품을 모니터링하고, 설정한 가격에 도달했을 때 알림을 보내는 시스템입니다.

## 주요 기능

- KREAM 상품 실시간 모니터링
- 설정한 가격 도달 시 알림 전송
- 사이즈별 가격 정보 확인
- 자동 로그인 기능

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install selenium beautifulsoup4 requests
```

## 사용 방법

1. `main.py` 파일에서 다음 정보를 설정:
   - `product_url`: 모니터링할 상품 URL
   - `target_price`: 목표 가격
   - `size`: 원하는 사이즈
   - `kream_id`: KREAM 계정 ID
   - `kream_pw`: KREAM 계정 비밀번호

2. `send_msg.py` 파일에서 다음 정보를 설정:
   - `token`: pushover api token
   - `user`: pushover user key

2. 프로그램 실행:
```bash
python main.py
```

## 파일 설명

- `main.py`: 메인 실행 파일 (Selenium을 사용한 모니터링)
- `send_msg.py`: 알림 전송 기능

## 주의사항

- KREAM의 정책에 따라 과도한 요청은 제한될 수 있습니다.
- 계정 정보는 보안을 위해 환경 변수로 관리하는 것을 권장합니다. 