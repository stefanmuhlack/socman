import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  userRole: string;

  constructor(private authService: AuthService, private playerRatingService: PlayerRatingService, private router: Router) {
    this.userRole = {} as any 
   }

  ngOnInit(): void {
    this.loadDashboard();
  }

  loadDashboard(): void {
    this.userRole = this.authService.getUserRole(); // Fetch user role from AuthService
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