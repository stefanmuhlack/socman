import { Component } from '@angular/core';
import { MatchFactService } from '../../services/match-fact.service';
import { MatchFact } from '../../models/match-fact.model';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-create-match-fact',
  templateUrl: './create-match-fact.component.html',
  imports: [CommonModule, FormsModule]
})
export class CreateMatchFactComponent {
  matchFact: MatchFact = {
    player_id: 0,
    kilometers_run: 0,
    sprints: 0,
    intensive_runs: 0,
    distance_run: 0,
    match_date: new Date()
  };

  constructor(private matchFactService: MatchFactService) { }

  createMatchFact() {
    this.matchFactService.createMatchFact(this.matchFact).subscribe(
      () => {
        // Handle success
      },
      error => {
        // Handle error
      }
    );
  }
}
