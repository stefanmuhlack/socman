# Stage 1: Build the Angular app with both browser and server bundles

# Use node image for building the Angular app
FROM node:18-alpine AS dev

RUN npm install -g @angular/cli

FROM node:18-alpine AS build

WORKDIR /app

# Copy the package.json and package-lock.json for installing dependencies
COPY frontend/package.json frontend/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the Angular application code
COPY frontend/ ./

# Build the Angular app
RUN npm run build --prod

# Stage 2: Serve the static files using Nginx for the client-side part (browser)
FROM nginx:alpine AS browser

# Copy the browser build from the previous stage to Nginx's default folder
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html

# Expose the port for Nginx (80 by default)
EXPOSE 80

# Start Nginx to serve the static files
CMD ["nginx", "-g", "daemon off;"]