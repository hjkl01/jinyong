FROM nginx:1.13.1
# Make NGINX run on the foreground
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Remove default configuration from Nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /cert
COPY viewer.pub.key /cert/
COPY viewer.pub.pem /cert/

# Copy the modified Nginx conf
COPY nginx.conf /etc/nginx/conf.d/

# CMD ["nginx-debug"]
CMD ["nginx", "-g", "daemon off;"]
