import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
  private apiUrl = 'http://localhost:8000/players';  // Adjust this URL based on your API

  constructor(private http: HttpClient) { }

  createPlayer(player: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/create`, player);
  }
}
