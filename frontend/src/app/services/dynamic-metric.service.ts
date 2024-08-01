import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { DynamicMetric } from '../models/dynamic-metric.model';

@Injectable({
  providedIn: 'root'
})
export class DynamicMetricService {
  private apiUrl = 'http://localhost:8000/dynamic-metrics/';

  constructor(private http: HttpClient) { }

  getDynamicMetrics(): Observable<DynamicMetric[]> {
    return this.http.get<DynamicMetric[]>(this.apiUrl);
  }

  createDynamicMetric(metric: DynamicMetric): Observable<DynamicMetric> {
    return this.http.post<DynamicMetric>(this.apiUrl, metric);
  }

  updateDynamicMetric(metric: DynamicMetric): Observable<DynamicMetric> {
    return this.http.put<DynamicMetric>(`${this.apiUrl}${metric.id}`, metric);
  }

  deleteDynamicMetric(metricId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}${metricId}`);
  }
}
