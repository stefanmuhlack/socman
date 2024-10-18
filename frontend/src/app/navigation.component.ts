import { Component } from '@angular/core';
import { AuthService } from './services/auth.service';  // Import the AuthService

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public isLoggedIn: boolean = false;
  public userRole: string = '';

  constructor(private authService: AuthService) {
    this.isLoggedIn = this.authService.isAuthenticated();
    this.userRole = this.authService.getUserRole();  // Fetch the user's role
  }

  public toggleLoginState() {
    this.isLoggedIn = !this.isLoggedIn;
  }
}
