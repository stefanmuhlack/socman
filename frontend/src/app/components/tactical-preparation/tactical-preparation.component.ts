import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { JerseyComponent } from '../jersey/jersey.component';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-tactical-preparation',
  templateUrl: './tactical-preparation.component.html',
  imports: [FormsModule, JerseyComponent, CommonModule]
})
export class TacticalPreparationComponent {
  // Handle player drag and drop for formations.
  draggedPlayer: any = null;
  formation = {
    name: '',
    comment_english: ''
  }
  
  formations = [
    {
      name: '',
      comment_english: '',
      positions: [{label: '', player: '', teamType: ''}]
    },
    {
      name: '',
      comment_english: '',
    }
  ]
  
  selectedFormation = {
    name: '',
    comment_english: '',
    positions: [{label: '', player: '', teamType: ''}]
  }

  formationPositions = [
    {label: '', player: '', teamType: ''}
  ]

  players = [
    { name: '', position: '' }
  ]

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

  createFormation() {
    // Create the formation with the tacticalService.
  }

  saveFormation() {
    // Save the formation with the tacticalService.
  }

  getJerseyColor(teamType: string): string{
    // TODO Get the jersey color
    return'';
  }
}
