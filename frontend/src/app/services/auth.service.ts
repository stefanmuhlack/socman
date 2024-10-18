import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }

  getUserRole(): string {
    // Fetch the user role from local storage or token (could be enhanced later)
    return localStorage.getItem('userRole') || 'player';
  }

  isAuthenticated(): boolean {
    // Simple check for token existence (replace with real implementation)
    return !!localStorage.getItem('authToken');
  }

  // Example additional method to handle super-admin privileges
  isSuperAdmin(): boolean {
    return this.getUserRole() === 'super-admin';
  }
}
