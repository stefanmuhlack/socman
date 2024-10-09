import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PlayerRating } from '../models/player-rating.model';

@Injectable({
  providedIn: 'root',
})
export class PlayerRatingService {
  private apiUrl = 'http://localhost:8000/players/';

  constructor(private http: HttpClient) {}

  getPlayerRatings(playerId: number): Observable<PlayerRating[]>{
    // TODO: Implement http get
    return {} as Observable<PlayerRating[]>
  }

  exportPlayerData(): Observable<Blob> {
    return this.http.get(`${this.apiUrl}/export`, { responseType: 'blob' });
  }

  createPlayerRating(PlayerRating: PlayerRating): Observable<PlayerRating>{
    // TODO: Implement http post
    return {} as Observable<PlayerRating>
  }
}
