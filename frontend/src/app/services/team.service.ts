import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TeamService {
  private apiUrl = 'http://localhost:8000/teams';  // Adjust this URL based on your API

  constructor(private http: HttpClient) { }

  createTeam(team: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/create`, team);
  }

  getClubs(): Observable<any> {
    return this.http.get('http://localhost:8000/clubs');  // URL for fetching clubs
  }
}
