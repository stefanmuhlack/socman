import { Component } from '@angular/core';
import { TournamentService } from '../../services/tournament.service';
import { Tournament } from '../../models/tournament.model';

@Component({
  selector: 'app-create-tournament',
  templateUrl: './create-tournament.component.html',
})
export class CreateTournamentComponent {
  tournament: Tournament = {
    name: '',
    type: 'knockout',  // Default tournament type
    group_stage: false,
    knockout_stage: true,
    admin_id: 0  // Admin ID will be set dynamically
  };

  constructor(private tournamentService: TournamentService) {}

  createTournament() {
    this.tournamentService.createTournament(this.tournament).subscribe(
      () => {
        // Success handling
      },
      error => {
        // Error handling
      }
    );
  }
}
