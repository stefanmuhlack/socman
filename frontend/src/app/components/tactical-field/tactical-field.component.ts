import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-tactical-field',
  templateUrl: './tactical-field.component.html',
})
export class TacticalFieldComponent {
  @Input() players: any[] = [];
  @Output() playerPositionChange = new EventEmitter<any>();

  // Emit the change when a player's position is modified
  onPlayerPositionChange(player: any, newPosition: string) {
    this.playerPositionChange.emit({ player, newPosition });
  }
}
