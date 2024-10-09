# Dockerfile for Frontend
FROM node:18-alpine AS build

WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy all source files
COPY  frontend/ ./

# Build the Angular app
RUN npm run build --prod

# Stage 2: Nginx to serve the Angular app
FROM nginx:alpine
COPY --from=build /app/dist/frontend /usr/share/nginx/html
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
