import { Component } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';
import { PlayerRating } from '../../models/player-rating.model';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-player-self-assessment',
  templateUrl: './player-self-assessment.component.html',
  imports: [FormsModule]
})
export class PlayerSelfAssessmentComponent {
  assessment = {} as PlayerRating;

  constructor(private playerRatingService: PlayerRatingService) { }

  submitAssessment() {
    this.playerRatingService.submitSelfAssessment(this.assessment).subscribe({
      next: () => {
        // Handle success
      },
      error: (error: Error) => {
        // Handle error
      },
      complete: () => { }
    }
    );
  }
}
