import { Component, OnInit } from '@angular/core';
import { NotificationService } from '../../services/notification.service';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  imports: [CommonModule],
})
export class NotificationComponent implements OnInit {
  notifications: string[] = [];

  constructor(private notificationService: NotificationService) {}

  ngOnInit(): void {
    this.notificationService.onMessage((message: string) => {
      this.notifications.push(message);
    });
  }
}
