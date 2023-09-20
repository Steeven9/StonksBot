FROM python:alpine

WORKDIR /usr/src/app
CMD [ "python", "./main.py" ]

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
