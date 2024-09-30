import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PlayerRatingHistory } from '../models/player-rating-history.model';

@Injectable({
  providedIn: 'root',
})
export class PlayerRatingService {
  private apiUrl = 'http://localhost:8000/players/';

  constructor(private http: HttpClient) {}

  getRatingHistory(playerId: number): Observable<PlayerRatingHistory[]> {
    return this.http.get<PlayerRatingHistory[]>(`${this.apiUrl}${playerId}/ratings/history/`);
  }
}
exportPlayerData(): Observable<Blob> {
  return this.http.get('/api/player/export', { responseType: 'blob' });
}

exportPlayerData(): Observable<Blob> {
  return this.http.get(`${this.apiUrl}/export`, { responseType: 'blob' });
}
