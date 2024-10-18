import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { PlayerRatingService } from '../../services/player-rating.service';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  imports: [CommonModule],
})
export class DashboardComponent implements OnInit {
  userRole: string;

  constructor(private authService: AuthService, private playerRatingService: PlayerRatingService, private router: Router) {
    this.userRole = '';
  }

  ngOnInit(): void {
    this.loadDashboard();
  }

  loadDashboard(): void {
    this.userRole = this.authService.getUserRole();  // Fetch user role from AuthService

    // Load specific data based on role
    if (this.userRole === 'super-admin') {
      // Load super-admin-specific data
    } else if (this.userRole === 'admin') {
      // Load admin-specific data
    } else if (this.userRole === 'coach') {
      // Load coach-specific data
    } else if (this.userRole === 'player') {
      // Load player-specific data
    }
  }

  exportPlayerData() {
    this.playerRatingService.exportPlayerData().subscribe((data) => {
      const blob = new Blob([data], { type: 'text/csv' });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'player-data.csv';
      a.click();
    });
  }
}