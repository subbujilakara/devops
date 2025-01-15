FROM nginx:1.19-alpine
ENV DEBIAN_FRONTEND=noninteractive
RUN addgroup -S nginx && adduser -S nginx -G nginx
COPY nginx.conf /etc/nginx/nginx.conf
RUN chown -R nginx:nginx /etc/nginx
EXPOSE 80 443
USER nginx
CMD ["nginx", "-g", "daemon off;"]
RUN rm -rf /var/cache/apk/*
LABEL maintainer="your-email@example.com" \
      version="1.19" \
      description="NGINX 1.19 with security best practices"
