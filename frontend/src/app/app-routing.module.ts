import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminManagementComponent } from './components/admin-management/admin-management.component';
import { CreateLeagueComponent } from './components/create-league/create-league.component';
import { CreateClubComponent } from './components/create-club/create-club.component';
import { CreateTeamComponent } from './components/create-team/create-team.component';
import { CreateCoachComponent } from './components/create-coach/create-coach.component';
import { CreatePlayerComponent } from './components/create-player/create-player.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { PlayerSelfAssessmentComponent } from './components/player-self-assessment/player-self-assessment.component';
import { AuthGuard } from './services/auth.guard';  // Ensure the AuthGuard is also imported

const routes: Routes = [
  { path: 'manage-admins', component: AdminManagementComponent, canActivate: [AuthGuard], data: { roles: ['super-admin'] } },
  { path: 'create-league', component: CreateLeagueComponent, canActivate: [AuthGuard], data: { roles: ['admin'] } },
  { path: 'create-club', component: CreateClubComponent, canActivate: [AuthGuard], data: { roles: ['admin'] } },
  { path: 'create-team', component: CreateTeamComponent, canActivate: [AuthGuard], data: { roles: ['admin'] } },
  { path: 'create-coach', component: CreateCoachComponent, canActivate: [AuthGuard], data: { roles: ['admin'] } },
  { path: 'create-player', component: CreatePlayerComponent, canActivate: [AuthGuard], data: { roles: ['coach'] } },
  { path: 'player-self-assessment', component: PlayerSelfAssessmentComponent, canActivate: [AuthGuard], data: { roles: ['player'] } },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard], data: { roles: ['super-admin', 'admin', 'coach', 'player'] } },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },  // Default route
  { path: '**', redirectTo: '/dashboard' }  // Wildcard route for handling 404s
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
