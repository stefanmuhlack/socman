import { Component, OnInit } from '@angular/core';
import { Chart } from 'chart.js';
import { PlayerRatingService } from '../../services/player-rating.service';
import { DynamicMetricService } from '../../services/dynamic-metric.service';
import { PlayerRating } from '../../models/player-rating.model';

@Component({
  selector: 'app-player-rating',
  templateUrl: './player-rating.component.html',
})

export class PlayerRatingComponent implements OnInit {
  constructor(
    private playerRatingService: PlayerRatingService,
    private dynamicMetricService: DynamicMetricService
  ) {
    this.availableMetrics = [];
    this.editMode = false;
    this.loadMetrics();
  }

  editMode: boolean;

  playerRating: PlayerRating = {
    player_id: 0,
    coach_id: 0,
    metrics: {} as { name: string, value: number}[],  // Metrics will be stored dynamically
    ballManipulation: 8,
    kickingAbility: 7,
    passingAbility: 9,
    duelTackling: 6,
    fieldCoverage: 7,
    blockingAbility: 8,
    gameStrategy: 7,
    playmakingRisk: 5,
    rating_date: new Date()
  };
  

  player = {
    name: 'Player 1',
    ratings: this.playerRating
  };

  ngOnInit() {
    this.loadSpiderChart();
  }
  
  availableMetrics: { name: string, value: number }[];

  toggleEditMode(){
    this.editMode = !this.editMode;
  }

  loadMetrics() {
    this.dynamicMetricService.getDynamicMetrics().subscribe((metrics) => {
      this.availableMetrics = metrics.map((metric) => ({
        name: metric.name,
        value: 0  // Default value for the rating
      }));
    });
  }

  loadSpiderChart() {
    const ctx = document.getElementById('spiderChart') as HTMLCanvasElement;
    new Chart(ctx, {
      type: 'radar',
      data: {
        labels: ['Ball Manipulation', 'Kicking Ability', 'Passing Ability', 'Duel Tackling', 'Field Coverage', 'Blocking Ability', 'Game Strategy', 'Playmaking Risk'],
        datasets: [{
          label: this.player.name + ' Performance',
          data: [
            this.player.ratings.ballManipulation,
            this.player.ratings.kickingAbility,
            this.player.ratings.passingAbility,
            this.player.ratings.duelTackling,
            this.player.ratings.fieldCoverage,
            this.player.ratings.blockingAbility,
            this.player.ratings.gameStrategy,
            this.player.ratings.playmakingRisk
          ],
          backgroundColor: 'rgba(0, 123, 255, 0.2)',
          borderColor: 'rgba(0, 123, 255, 1)',
        }]
      },
      options: {
        scale: {
          ticks: { beginAtZero: true }
        }
      }
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

  downloadPlayerData() {
    this.playerRatingService.exportPlayerData().subscribe(blob => {
      const a = document.createElement('a');
      const objectUrl = URL.createObjectURL(blob);
      a.href = objectUrl;
      a.download = 'players.csv';
      a.click();
      URL.revokeObjectURL(objectUrl);
    });
  }

}