import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }

  getUserRole(): string {
    // Example: Assuming you have the user role stored in local storage after login
    return localStorage.getItem('userRole') || '';
  }

  // Additional Auth-related methods
}
