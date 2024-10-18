import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { PlayerTeam } from '../models/player-team.model';

@Injectable({
  providedIn: 'root'
})
export class PlayerTeamService {
  private apiUrl = 'http://localhost:8000/player-teams/';

  constructor(private http: HttpClient) {}

  getPlayerTeams(playerId: number): Observable<PlayerTeam[]> {
    return this.http.get<PlayerTeam[]>(`${this.apiUrl}${playerId}`);
  }

  addPlayerToTeam(playerTeam: PlayerTeam): Observable<PlayerTeam> {
    return this.http.post<PlayerTeam>(this.apiUrl, playerTeam);
  }

  setActiveTeam(playerId: number, teamId: number): Observable<PlayerTeam> {
    return this.http.put<PlayerTeam>(`${this.apiUrl}${playerId}/active`, { teamId });
  }
}