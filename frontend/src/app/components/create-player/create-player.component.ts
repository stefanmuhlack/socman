import { Component, OnInit } from '@angular/core';
import { PlayerService } from '../../services/player.service';
import { FormsModule, NgForm } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-create-player',
  templateUrl: './create-player.component.html',
  styleUrls: ['./create-player.component.css'],
  imports: [CommonModule, FormsModule]
})
export class CreatePlayerComponent implements OnInit {
  player: any = {
    name: '',
    jersey_number: null,
    position: 'TW',
    is_captain: false,
    start_lineup: false
  };

  constructor(private playerService: PlayerService) { }

  ngOnInit(): void {
    // Any initialization logic can go here
  }

  createPlayer(form: NgForm): void {
    if (form.valid) {
      this.playerService.createPlayer(this.player).subscribe(
        (response: Response) => {
          console.log('Player created successfully', response);
          form.reset();
        },
        (error: Error) => {
          console.error('Error creating player', error);
        }
      );
    }
  }
}
