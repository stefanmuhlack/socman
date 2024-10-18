// src/app/app.config.server.ts
import { ApplicationConfig, Provider } from '@angular/core';

export const API_ENDPOINT = 'apiEndpoint';  // Define a token for the API endpoint

export const config: ApplicationConfig = {
  providers: [
    { provide: API_ENDPOINT, useValue: 'https://api.example.com' },
    // Add other server-specific providers here if needed
  ]
};
