FROM rishabhc32/node-python-alpine:v2

RUN rm app.js
ADD app.js package.json index.html package-lock.json /app/
ADD public /app/public
RUN npm install

EXPOSE 8080

CMD ["node", "app.js"]
