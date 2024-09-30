import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CustomMetricService {
  constructor(private http: HttpClient) { }

  createCustomMetric(metric: any) {
    return this.http.post('/api/custom-metric', metric);
  }
}
