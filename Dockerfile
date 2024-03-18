FROM nginx:1.25-alpine

COPY /nginx/html /usr/share/nginx/html
COPY /patterns /usr/share/nginx/html/patterns

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]