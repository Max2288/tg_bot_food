FROM nginx:1.18

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf /etc/nginx/conf.d
CMD ["nginx", "-g", "daemon off;"]