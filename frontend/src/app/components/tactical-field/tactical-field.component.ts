import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-tactical-field',
  templateUrl: './tactical-field.component.html',
})
export class TacticalFieldComponent {
  @Input() players: any[] = [];
  @Output() playerPositionChange = new EventEmitter<any>();

  draggedPlayer: any;

  // Handle dragging the player
  onDragStart(player: any) {
    this.draggedPlayer = player;
  }

  // Allow the drop event
  allowDrop(event: any) {
    event.preventDefault();
  }

  // Handle dropping the player into a new position
  onDrop(targetPlayer: any) {
    const draggedPlayerPosition = this.draggedPlayer.position;
    this.draggedPlayer.position = targetPlayer.position;
    targetPlayer.position = draggedPlayerPosition;

    // Emit the position change
    this.playerPositionChange.emit({
      player: this.draggedPlayer,
      target: targetPlayer,
    });

    // Clear the dragged player
    this.draggedPlayer = null;
  }
}
