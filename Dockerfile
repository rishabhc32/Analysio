FROM rishabhc32/node-python-alpine:latest

RUN rm app.js
ADD ./app.js /app/

CMD ["node", "app.js"]
