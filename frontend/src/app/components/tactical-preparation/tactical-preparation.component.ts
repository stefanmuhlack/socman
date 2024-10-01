import { Component } from '@angular/core';

@Component({
  selector: 'app-tactical-preparation',
  templateUrl: './tactical-preparation.component.html',
})
export class TacticalPreparationComponent {
  // Handle player drag and drop for formations.
  draggedPlayer: any = null;

  onDragStart(player: any) {
    this.draggedPlayer = player;
  }

  allowDrop(event: any) {
    event.preventDefault();
  }

  onDrop(position: any) {
    position.player = this.draggedPlayer;
    this.draggedPlayer = null;
  }

  saveFormation() {
    // Save the formation with the tacticalService.
  }
}
