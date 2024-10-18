import { Component, Input } from '@angular/core';

@Component({
  standalone: true,
  selector: 'app-tactical-field',
  templateUrl: './tactical-field.component.html',
})
export class TacticalFieldComponent {
  @Input() formationPositions: any[] = [];
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

  getJerseyColor(teamType: string) {
    return teamType === 'home' ? 'blue' : 'red'; // Adjust to dynamically load jersey colors
  }
}
