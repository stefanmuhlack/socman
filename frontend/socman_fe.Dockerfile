# Stage 1: Build the Angular app with both browser and server bundles

# Use node image for building the Angular app
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

# Stage 2: Serve the Angular Universal app with Nginx for browser and Node.js for SSR

# Use a minimal Node.js image to serve the server-side part (SSR)
FROM node:18-alpine AS server

WORKDIR /app

# Copy the server build from the previous stage
COPY --from=build /app/dist/frontend/server ./server
COPY --from=build /app/node_modules ./node_modules

# Expose the port on which the SSR server will run
EXPOSE 4000

# Command to run the server-side rendering
CMD ["node", "server/server.mjs"]

# Stage 3: Serve the static files using Nginx for the client-side part (browser)
FROM nginx:alpine AS browser

# Copy the browser build from the previous stage to Nginx's default folder
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html

# Expose the port for Nginx (80 by default)
EXPOSE 80

# Start Nginx to serve the static files
CMD ["nginx", "-g", "daemon off;"]