import { Component, OnInit } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-tournament-leaderboard',
  templateUrl: './tournament-leaderboard.component.html',
  imports: [CommonModule]
})
export class TournamentLeaderboardComponent implements OnInit {
  leaderboard: any[] = [];
  tournaments: any[] = [];
  currentPage = 1;
  pageSize = 10;
  totalItems = 0;
  tournamentId = 0;

  constructor(private tournamentService: TournamentService) {}

  ngOnInit() {
    this.loadLeaderboard(this.currentPage, this.pageSize);
  }
  onTournamentSelectChange(event: Event){
    let target = event.target as HTMLElement;
    if (target === null) return;

    let val = parseInt(target.textContent || "");
    if (isNaN(val)) return;
    
    this.loadLeaderboard(val)
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
