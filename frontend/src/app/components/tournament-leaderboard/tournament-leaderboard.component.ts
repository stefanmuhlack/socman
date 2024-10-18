import { Component, OnInit } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';

@Component({
  selector: 'app-tournament-leaderboard',
  templateUrl: './tournament-leaderboard.component.html',
})
export class TournamentLeaderboardComponent implements OnInit {
  leaderboard: any[] = [];
  currentPage = 1;
  pageSize = 10;
  totalItems = 0;
  tournamentId = 0;

  constructor(private tournamentService: TournamentService) {}

  ngOnInit() {
    this.loadLeaderboard(this.currentPage, this.pageSize);
  }

  loadLeaderboard(page: number, pageSize: number = this.pageSize): void {
    this.tournamentService.getLeaderboard(this.tournamentId, page, pageSize).subscribe((data) => {
      this.leaderboard = data.items;  // assuming the backend returns an object with items and totalItems
      this.totalItems = data.totalItems;
    });
  }

getMaxPages(): number {
  return Math.ceil(this.totalItems / this.pageSize);
}

  
  onPageChange(page: number): void {
    this.currentPage = page;
    this.loadLeaderboard(this.currentPage, this.pageSize);
  }
}
