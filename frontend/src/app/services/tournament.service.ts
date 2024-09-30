import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TournamentService {
  private apiUrl = 'http://localhost:8000/tournaments/';

  constructor(private http: HttpClient) {}

  getLeaderboard(tournamentId: number, page: number, pageSize: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${tournamentId}/leaderboard?page=${page}&page_size=${pageSize}`);
  }
}
