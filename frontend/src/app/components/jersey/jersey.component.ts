import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  standalone: true,
  selector: 'app-jersey',
  templateUrl: './jersey.component.html',
  imports: [CommonModule],
  })
export class JerseyComponent {
  @Input() player: any;
  @Input() jerseyColor: string = '';
}