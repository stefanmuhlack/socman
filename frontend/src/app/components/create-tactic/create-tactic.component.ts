import { Component } from '@angular/core';
import { TacticService } from '../../services/tactic.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  standalone: true,
  selector: 'app-create-tactic',
  templateUrl: './create-tactic.component.html',
  imports: [CommonModule, FormsModule]
})
export class CreateTacticComponent {
  tactics = {
    formation: '4-4-2',
    positions: [
      { position: 'GK', player_id: null },
      { position: 'LB', player_id: null },
      { position: 'CB', player_id: null },
      // More positions...
    ]
  };

  constructor(private tacticsService: TacticService) {}

  saveTactic() {
    if (!this.tactics.positions.every(pos => pos.player_id)) {
      alert('Please assign all players to valid positions.');
      return;
    }
    this.tacticsService.saveTactic(this.tactics).subscribe({
      next: () => {
        // Success handling
      },
      error: (err: Error) => {
        alert('Error saving tactic: ' + err.message);
      }
    });
  }
}
