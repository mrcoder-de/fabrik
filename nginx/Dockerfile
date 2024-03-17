# Use Nginx image from Docker Hub
FROM nginx:latest

# Copy static files to Nginx
COPY /html /usr/share/nginx/html
COPY /patterns /usr/share/nginx/html/patterns

# Expose ports
EXPOSE 80

# Start Nginx when container is created
CMD ["nginx", "-g", "daemon off;"]