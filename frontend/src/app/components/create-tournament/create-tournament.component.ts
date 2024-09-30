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
    type: 'liga',  // Default to 'liga' type
    teams_number: 18,  // Example default
    home_away: false,
    best_teams_promoted: 2,
    worst_teams_relegated: 2,
    third_place_playoff: false,
    penalty_shootout: false,
    promotion_to: null,
    relegation_to: null
  };

  constructor(private tournamentService: TournamentService) {}

  createTournament() {
    this.tournamentService.createTournament(this.tournament).subscribe(() => {
      // Success handling
    });
  }
}
