import { Component, OnInit } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';

@Component({
  selector: 'app-tournament-leaderboard',
  templateUrl: './tournament-leaderboard.component.html',
})
export class TournamentLeaderboardComponent implements OnInit {
  leaderboard: any[] = [];

  constructor(private tournamentService: TournamentService) {}

  ngOnInit(): void {
    this.loadLeaderboard();
  }

  loadLeaderboard(tournamentId: number): void {
  this.tournamentService.getLeaderboard(tournamentId).subscribe((data) => {
    this.leaderboard = data;
  });
}
}
