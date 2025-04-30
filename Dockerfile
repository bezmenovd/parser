FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip curl libnss3 libxss1 libasound2 libatk1.0-0 \
    libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    && apt-get clean

RUN wget https://storage.googleapis.com/chrome-for-testing-public/114.0.5735.90/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    mv chrome-linux64 /opt/chrome && \
    ln -s /opt/chrome/chrome /usr/bin/google-chrome && \
    rm chrome-linux64.zip

RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

RUN pip install --no-cache-dir undetected-chromedriver==3.4.6 selenium==4.9.1

RUN apt-get install -y libdrm2 libgbm1 xvfb \
    && apt-get clean

WORKDIR /app
COPY main.py .

CMD ["python", "main.py"]
