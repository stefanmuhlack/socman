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

if (!this.tactics.positions.every(pos => pos.player_id)) {
  alert('Please assign all players to valid positions.');
  return;
}

  
  saveTactic() {
    this.tacticalService.saveTactic(this.tactics).subscribe(() => {
      // Success handling
    });
  }
}
