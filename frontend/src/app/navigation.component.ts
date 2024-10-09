import { Component } from '@angular/core';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public isLoggedIn: boolean = false;

  // Example method to toggle login state or fetch data.
  public toggleLoginState() {
    this.isLoggedIn = !this.isLoggedIn;
  }
}
