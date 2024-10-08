# Use Node.js image to build Angular
FROM node:14 as build

# Set working directory
WORKDIR /app

# Install dependencies
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install

# Copy the rest of the app code
COPY frontend/ .

# Build the Angular app
RUN npm run build --prod

# Use Nginx to serve the built Angular app
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80
