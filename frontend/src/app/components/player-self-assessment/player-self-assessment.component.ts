import { Component } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';

@Component({
  selector: 'app-player-self-assessment',
  templateUrl: './player-self-assessment.component.html',
})
export class PlayerSelfAssessmentComponent {
  assessment = {
    player_id: 0,
    metrics: {}
  };

  constructor(private playerRatingService: PlayerRatingService) {}

  submitAssessment() {
    this.playerRatingService.submitSelfAssessment(this.assessment).subscribe(
      () => {
        // Handle success
      },
      (error) => {
        // Handle error
      }
    );
  }
}
