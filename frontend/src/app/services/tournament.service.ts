import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TournamentService {
  private apiUrl = 'http://localhost:8000/tournaments/';

  constructor(private http: HttpClient) {}

  createTournament(tournament: any): Observable<any> {
    return this.http.post(this.apiUrl, tournament);
  }

 getLeaderboard(tournamentId: number): Observable<any> {
   return this.http.get(`${this.apiUrl}${tournamentId}/leaderboard`);
 }

  
  applyPromotionRelegation(tournamentId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/promotion-relegation/`, { tournament_id: tournamentId });
  }
}
