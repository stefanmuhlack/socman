import { Component } from '@angular/core';

@Component({
  selector: 'app-tactical-preparation',
  templateUrl: './tactical-preparation.component.html',
})
export class TacticalPreparationComponent {
  selectedFormation = { name: '4-4-2' }; // Example formation
  players = [
    { id: 1, name: 'Player 1', position: 'LV' },
    { id: 2, name: 'Player 2', position: 'IVL' },
    // more players
  ];
  formationPositions = [
    { label: 'LV', player: null, teamType: 'home' }, // For each position
    { label: 'IVL', player: null, teamType: 'home' },
    // Define more positions based on the selected formation
  ];

  draggedPlayer: any = null;

  // Function to start dragging
  onDragStart(player: any) {
    this.draggedPlayer = player;
  }

  // Allow drop
  allowDrop(event: any) {
    event.preventDefault();
  }

  // Drop player into position
  onDrop(position: any) {
    position.player = this.draggedPlayer;
    this.draggedPlayer = null; // Reset the dragged player
  }

  // Save the current formation
  saveFormation() {
    const formationData = {
      formationName: this.selectedFormation.name,
      positions: this.formationPositions.map(p => ({
        position: p.label,
        player_id: p.player ? p.player.id : null
      })),
    };

    this.tacticalService.createFormation(formationData).subscribe(() => {
      alert('Formation saved successfully!');
    });
  }

  // Dynamically get jersey color based on team type
  getJerseyColor(teamType: string) {
    return teamType === 'home' ? this.homeJerseyColor : this.awayJerseyColor;
  }
}
