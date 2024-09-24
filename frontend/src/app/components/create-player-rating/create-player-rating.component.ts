import { Component } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';
import { PlayerRating } from '../../models/player-rating.model';
import { DynamicMetricService } from '../../services/dynamic-metric.service';

@Component({
  selector: 'app-create-player-rating',
  templateUrl: './create-player-rating.component.html',
})
export class CreatePlayerRatingComponent {
  playerRating: PlayerRating = {
    player_id: 0,
    coach_id: 0,
    metrics: {},  // Metrics will be stored dynamically
    rating_date: new Date()
  };

  availableMetrics: { name: string, value: number }[] = [];

  constructor(
    private playerRatingService: PlayerRatingService,
    private dynamicMetricService: DynamicMetricService
  ) {
    this.loadMetrics();
  }

  loadMetrics() {
    this.dynamicMetricService.getDynamicMetrics().subscribe((metrics) => {
      this.availableMetrics = metrics.map((metric) => ({
        name: metric.name,
        value: 0  // Default value for the rating
      }));
    });
  }

  createPlayerRating() {
    // Convert metrics array into a dictionary
    this.playerRating.metrics = this.availableMetrics.reduce((acc, metric) => {
      acc[metric.name] = metric.value;
      return acc;
    }, {});

    this.playerRatingService.createPlayerRating(this.playerRating).subscribe(
      () => {
        // Success handling (e.g., redirect, display success message)
      },
      error => {
        // Error handling
      }
    );
  }
}
