FROM nginx

ENV HOST=0.0.0.0
ENV PORT=80

WORKDIR /usr/share/nginx/html
COPY dist/frontend ./
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
