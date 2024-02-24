FROM nginx:1.25

WORKDIR /usr/share/nginx/html

# Copy your index.html file
COPY index.html .