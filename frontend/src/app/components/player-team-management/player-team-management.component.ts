import { Component, OnInit } from '@angular/core';
import { PlayerTeamService } from '../../services/player-team.service';
import { PlayerTeam } from '../../models/player-team.model';

@Component({
  standalone: true,
  selector: 'app-player-team-management',
  templateUrl: './player-team-management.component.html',
})
export class PlayerTeamManagementComponent implements OnInit {
  playerTeams: PlayerTeam[] = [];
  newPlayerTeam: PlayerTeam = {
    player_id: 0,
    team_id: 0,
    role: 'primary',  // Default to primary role
  };

  constructor(private playerTeamService: PlayerTeamService) {}

  ngOnInit(): void {
    this.loadPlayerTeams();
  }

  loadPlayerTeams() {
    this.playerTeamService.getPlayerTeams(this.newPlayerTeam.player_id).subscribe(
      (data) => {
        this.playerTeams = data;
      },
      (error) => {
        // Handle error
      }
    );
  }

  addPlayerToTeam() {
    this.playerTeamService.addPlayerToTeam(this.newPlayerTeam).subscribe(
      () => {
        // Refresh the player-team list after adding
        this.loadPlayerTeams();
      },
      (error) => {
        // Handle error
      }
    );
  }
}
