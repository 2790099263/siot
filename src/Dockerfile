FROM python:3.8
EXPOSE 5000
WORKDIR /root/src
CMD pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 install --upgrade pip && \
    pip3 install pymysql && \
    pip3 install flask && \
    python3 app.py