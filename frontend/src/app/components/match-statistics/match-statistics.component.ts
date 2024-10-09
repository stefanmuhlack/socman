import { Component } from '@angular/core';
import { MatchStatisticsService } from '../../services/match-statistics.service';

@Component({
})
export class CreateMatchStatisticsComponent {
  statistics = {
    match_id: 0,
    player_id: 0,
    goals: 0,
    assists: 0,
    tackles: 0,
    passes_completed: 0,
    fouls_committed: 0,
    minutes_played: 0,
    team_id: 0
  };

  constructor(private matchStatisticsService: MatchStatisticsService) {}

  submitStatistics() {
    this.matchStatisticsService.submitStatistics(this.statistics).subscribe(
      () => {
        // Handle success
      },
      (error) => {
        // Handle error
      }
    );
  }
}
