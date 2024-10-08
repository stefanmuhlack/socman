import { Component } from '@angular/core';
import { TacticalService } from '../../services/tactical.service';

@Component({
  selector: 'app-create-tactic',
  templateUrl: './create-tactic.component.html',
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

  constructor(private tacticalService: TacticalService) {}

  saveTactic() {
    if (!this.tactics.positions.every(pos => pos.player_id)) {
      alert('Please assign all players to valid positions.');
      return;
    }
    this.tacticalService.saveTactic(this.tactics).subscribe({
      next: () => {
        // Success handling
      },
      error: (err) => {
        alert('Error saving tactic: ' + err.message);
      }
    });
  }
}
