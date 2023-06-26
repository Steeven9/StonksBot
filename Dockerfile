FROM python:3

WORKDIR /usr/src/app
CMD [ "python", "./main.py" ]

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
