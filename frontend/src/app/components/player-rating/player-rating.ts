import { Component, OnInit } from '@angular/core';
import { Chart } from 'chart.js';

@Component({
  selector: 'app-player-rating',
  templateUrl: './player-rating.component.html',
})
export class PlayerRatingComponent implements OnInit {
  player = {
    name: 'Player 1',
    ratings: {
      ballManipulation: 8,
      kickingAbility: 7,
      passingAbility: 9,
      duelTackling: 6,
      fieldCoverage: 7,
      blockingAbility: 8,
      gameStrategy: 7,
      playmakingRisk: 5,
    }
  };

  ngOnInit() {
    this.loadSpiderChart();
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
