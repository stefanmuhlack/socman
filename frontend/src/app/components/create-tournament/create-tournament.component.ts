import { Component } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';
import { Tournament } from '../../models/tournament.model';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-create-tournament',
  templateUrl: './create-tournament.component.html',
  imports: [FormsModule, CommonModule]
})
export class CreateTournamentComponent {
  tournament = {
    name: '',
    type: 'liga',
    teams_number: 18,
    home_away: false,
    best_teams_promoted: 2,
    worst_teams_relegated: 2,
    third_place_playoff: false,
    penalty_shootout: false,
    max_starting_players: 11,
    max_substitutes: 5,
    substitution_limit: 3
  };
  errorMessage = '';

  constructor(private tournamentService: TournamentService) {}

  createTournament() {
    if (!this.tournament.name || this.tournament.teams_number <= 0) {
      this.errorMessage = 'Tournament name and team number must be valid.';
      return;
    }

    this.tournamentService.createTournament(this.tournament).subscribe({
      next: () => {
        // Handle success
      },
      error: (err: Error) => {
        alert('Error creating tournament: ' + err.message);
      }
    });
  }
}
