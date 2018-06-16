FROM alpine:latest

WORKDIR /app

ADD ./diabetes.csv ./diabetes.py ./app.js ./requirements.txt /app/


RUN apk --update add --no-cache lapack-dev gcc freetype-dev python3-dev

RUN apk add --no-cache --virtual .build-deps gfortran musl-dev g++
RUN  ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN apk add --update-cache nodejs
RUN apk add --update-cache python3
RUN pip3 install --upgrade pip

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN apk del .build-deps

CMD ["node", "app.js"]
