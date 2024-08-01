import { Component, OnInit, Input } from '@angular/core';
import { ChartData, ChartOptions } from 'chart.js';
import { PlayerRatingService } from '../../services/player-rating.service';
import { PlayerRating } from '../../models/player-rating.model';

@Component({
  selector: 'app-player-rating-chart',
  templateUrl: './player-rating-chart.component.html',
})
export class PlayerRatingChartComponent implements OnInit {
  @Input() playerId: number;

  radarChartOptions: ChartOptions = {
    responsive: true,
  };

  radarChartLabels: string[] = [
    'Ball Manipulation',
    'Kicking Ability',
    'Passing Ability',
    'Duel Tackling',
    'Field Coverage',
    'Blocking Ability',
    'Game Strategy',
    'Playmaking Risk'
  ];

  radarChartData: ChartData<'radar'> = {
    labels: this.radarChartLabels,
    datasets: [],
  };

  constructor(private playerRatingService: PlayerRatingService) {}

  ngOnInit(): void {
    this.loadPlayerRatings();
  }

  loadPlayerRatings() {
    this.playerRatingService.getPlayerRatings(this.playerId).subscribe((ratings: PlayerRating[]) => {
      const data = ratings.map(rating => {
        return this.radarChartLabels.map(label => rating.metrics[label]);
      });

      this.radarChartData = {
        labels: this.radarChartLabels,
        datasets: [
          {
            data: data.length ? data[0] : [],
            label: 'Player Performance',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
          },
        ],
      };
    });
  }
}
