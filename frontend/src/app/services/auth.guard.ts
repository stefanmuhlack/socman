import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, Router } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot): boolean {
    const expectedRoles = route.data['roles'];  // Fetch the expected roles from the route
    const userRole = this.authService.getUserRole();  // Get the user's role from AuthService

    if (this.authService.isAuthenticated() && expectedRoles.includes(userRole)) {
      return true;
    } else {
      this.router.navigate(['login']);
      return false;
    }
  }
}
