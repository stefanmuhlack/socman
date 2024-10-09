// src/app/app.config.ts
import { ApplicationConfig, Provider } from '@angular/core';

export const API_ENDPOINT = 'apiEndpoint';  // Define a token for the API endpoint

export const appConfig: ApplicationConfig = {
  providers: [
    { provide: API_ENDPOINT, useValue: 'https://api.example.com' },
    // Add other providers here if needed
  ]
};
