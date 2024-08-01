import { Component, OnInit } from '@angular/core';
import { ChartData, ChartOptions } from 'chart.js';

@Component({
  selector: 'app-player-rating-chart',
  templateUrl: './player-rating-chart.component.html',
})
export class PlayerRatingChartComponent implements OnInit {
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
    datasets: [
      {
        data: [8, 7, 6, 5, 9, 8, 7, 6],
        label: 'Player Performance',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      },
    ],
  };

  constructor() {}

  ngOnInit(): void {}
}
