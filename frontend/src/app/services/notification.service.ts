import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  private ws: WebSocket;

  constructor() {
    this.ws = new WebSocket('ws://localhost:8000/ws/notifications');
  }

  onMessage(callback: (message: string) => void) {
    this.ws.onmessage = (event) => {
      callback(event.data);
    };
  }

  sendMessage(message: string) {
    this.ws.send(message);
  }
}
