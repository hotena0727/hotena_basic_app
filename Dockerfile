FROM python:3.11-slim

WORKDIR /app

# (선택) 빌드 속도/호환성 보강
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cloud Run은 PORT 환경변수로 포트를 줌
ENV PORT=8080

# Streamlit 설정: 외부접속 허용 + 포트 반영
CMD ["bash", "-lc", "streamlit run hotena_basic.py --server.address=0.0.0.0 --server.port=$PORT --server.headless=true --server.enableCORS=false"]
