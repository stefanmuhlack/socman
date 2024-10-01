import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-jersey',
  templateUrl: './jersey.component.html',
})
export class JerseyComponent {
  @Input() player: any;
  @Input() jerseyColor: string;
}
