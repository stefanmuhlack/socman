import { Component, OnInit } from '@angular/core';
import { TeamService } from '../../services/team.service';
import { FormsModule, NgForm } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-create-team',
  templateUrl: './create-team.component.html',
  styleUrls: ['./create-team.component.css'],
  imports: [CommonModule, FormsModule]
})
export class CreateTeamComponent implements OnInit {
  team: any = {
    name: '',
    club_id: null,
    tactical_formation: '4-4-2',
    home_jersey_main_color: '',
    home_jersey_secondary_color: '',
    home_jersey_number_color: '',
    away_jersey_main_color: '',
    away_jersey_secondary_color: '',
    away_jersey_number_color: ''
  };

  clubs: any[] = [];  // Will be populated with actual club data

  constructor(private teamService: TeamService) { }

  ngOnInit(): void {
    // Fetch clubs to populate the dropdown
    this.teamService.getClubs().subscribe((data: any) => {
      this.clubs = data;
    });
  }

  createTeam(form: NgForm): void {
    if (form.valid) {
      this.teamService.createTeam(this.team).subscribe(
        (response: Response) => {
          console.log('Team created successfully', response);
          form.reset();
        },
        (error: Error) => {
          console.error('Error creating team', error);
        }
      );
    }
  }
}
