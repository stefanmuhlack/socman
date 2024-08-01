import { Component } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';
import { PlayerRating } from '../../models/player-rating.model';

@Component({
  selector: 'app-create-player-rating',
  templateUrl: './create-player-rating.component.html',
})
export class CreatePlayerRatingComponent {
  playerRating: PlayerRating = {
    player_id: 0,
    coach_id: 0,
    ball_manipulation: 0,
    kicking_ability: 0,
    passing_ability: 0,
    duel_tackling: 0,
    field_coverage: 0,
    blocking_ability: 0,
    game_strategy: 0,
    playmaking_risk: 0,
    rating_date: new Date()
  };

  constructor(private playerRatingService: PlayerRatingService) { }

  createPlayerRating() {
    this.playerRatingService.createPlayerRating(this.playerRating).subscribe(
      () => {
        // Handle success
      },
      error => {
        // Handle error
      }
    );
  }
}
