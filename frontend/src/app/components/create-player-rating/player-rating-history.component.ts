import { Component, OnInit, Input } from '@angular/core';
import { PlayerRatingService } from '../../services/player-rating.service';
import { ChartData, ChartOptions } from 'chart.js';

@Component({
  selector: 'app-player-rating-history',
  templateUrl: './player-rating-history.component.html',
})
export class PlayerRatingHistoryComponent implements OnInit {
  @Input() playerId: number;

  chartOptions: ChartOptions = {
    responsive: true,
  };

  chartData: ChartData<'line'> = {
    labels: [],
    datasets: [
      {
        data: [],
        label: 'Player Rating History',
        fill: false,
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  constructor(private playerRatingService: PlayerRatingService) {}

  ngOnInit(): void {
    this.loadRatingHistory();
  }

  loadRatingHistory(): void {
    this.playerRatingService.getRatingHistory(this.playerId).subscribe((history) => {
      const labels = history.map((entry) => new Date(entry.timestamp).toLocaleDateString());
      const data = history.map((entry) => entry.metrics.ball_manipulation); // Example metric

      this.chartData = {
        labels: labels,
        datasets: [
          {
            data: data,
            label: 'Ball Manipulation Over Time',
            fill: false,
            borderColor: 'rgba(75,192,192,1)',
          },
        ],
      };
    });
  }
}
