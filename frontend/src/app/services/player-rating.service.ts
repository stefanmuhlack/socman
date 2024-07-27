import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PlayerRating } from './player-rating.model';

@Injectable({
  providedIn: 'root'
})
export class PlayerRatingService {
  private apiUrl = 'http://localhost:8000/player-ratings/';

  constructor(private http: HttpClient) { }

  createPlayerRating(playerRating: PlayerRating): Observable<PlayerRating> {
    return this.http.post<PlayerRating>(this.apiUrl, playerRating);
  }

  getPlayerRatings(playerId: number): Observable<PlayerRating[]> {
    return this.http.get<PlayerRating[]>(`${this.apiUrl}${playerId}`);
  }
}
