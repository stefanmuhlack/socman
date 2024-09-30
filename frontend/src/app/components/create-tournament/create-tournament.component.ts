import { Component } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';
import { Tournament } from '../../models/tournament.model';

@Component({
  selector: 'app-create-tournament',
  templateUrl: './create-tournament.component.html',
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
  max_starting_players: 11,  // Default value
  max_substitutes: 5,  // Default value
  substitution_limit: 3  // Default value
};

  constructor(private tournamentService: TournamentService) {}

  createTournament() {
  this.tournamentService.createTournament(this.tournament).subscribe({
    next: () => {
      // Success feedback
    },
    error: (err) => {
      alert('Error creating tournament: ' + err.message);  // Simple error feedback
    }
  });
}
