import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MatchStatistics } from '../models/match-statistics.model';

@Injectable({
  providedIn: 'root'
})
export class MatchStatisticsService {
  private apiUrl = 'http://localhost:8000/match-statistics/';

  constructor(private http: HttpClient) { }

  createMatchStatistics(MatchStatistics: MatchStatistics): Observable<MatchStatistics> {
    return this.http.post<MatchStatistics>(this.apiUrl, MatchStatistics);
  }

  getMatchStatisticss(skip: number = 0, limit: number = 10): Observable<MatchStatistics[]> {
    return this.http.get<MatchStatistics[]>(`${this.apiUrl}?skip=${skip}&limit=${limit}`);
  }

  getMatchStatistics(MatchStatisticsId: number): Observable<MatchStatistics> {
    return this.http.get<MatchStatistics>(`${this.apiUrl}${MatchStatisticsId}`);
  }

  submitStatistics(MatchStatistics: MatchStatistics): Observable<MatchStatistics> {
    return this.http.patch<MatchStatistics>(`${this.apiUrl}${MatchStatistics.match_id}`, MatchStatistics);
  }
}
