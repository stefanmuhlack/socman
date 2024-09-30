import { Component, OnInit } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';

@Component({
  selector: 'app-player-rating-history',
  templateUrl: './player-rating-history.component.html',
})
export class PlayerRatingHistoryComponent implements OnInit {
  ratingHistory: any[] = [];

  constructor(private playerRatingService: PlayerRatingService) {}

  ngOnInit(): void {
    this.loadRatingHistory();
  }

  loadRatingHistory(): void {
    this.playerRatingService.getRatingHistory(1).subscribe(history => {
      this.ratingHistory = history;
    });
  }
}
