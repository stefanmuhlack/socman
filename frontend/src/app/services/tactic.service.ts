import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tactic } from '../models/tactic.model';

@Injectable({
  providedIn: 'root',
})
export class TacticService {
  private apiUrl = 'http://localhost:8000/tactic/';

  constructor(private http: HttpClient) {}

  get(): Observable<Tactic[]>{
    // TODO Implement Http Get Index
    return {} as Observable<Tactic[]>
  }

  saveTactic(tactic: Tactic): Observable<Tactic> {
    // TODO Implement Http Put
    return {} as Observable<Tactic>;
  }

}
