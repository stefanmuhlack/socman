import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MatchFact } from '../models/match-fact.model';

@Injectable({
  providedIn: 'root'
})
export class MatchFactService {
  private apiUrl = 'http://localhost:8000/match-facts/';

  constructor(private http: HttpClient) { }

  createMatchFact(matchFact: MatchFact): Observable<MatchFact> {
    return this.http.post<MatchFact>(this.apiUrl, matchFact);
  }

  getMatchFacts(skip: number = 0, limit: number = 10): Observable<MatchFact[]> {
    return this.http.get<MatchFact[]>(`${this.apiUrl}?skip=${skip}&limit=${limit}`);
  }

  getMatchFact(matchFactId: number): Observable<MatchFact> {
    return this.http.get<MatchFact>(`${this.apiUrl}${matchFactId}`);
  }
}
