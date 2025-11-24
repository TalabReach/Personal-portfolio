# Use official nginx image
FROM nginx:alpine
# Copy your project to nginx folder
COPY . /usr/share/nginx/html
#Port
EXPOSE 80