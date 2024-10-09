import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TacticalPreparationComponent } from './components/tactical-preparation/tactical-preparation.component';
import { TournamentLeaderboardComponent } from './components/tournament-leaderboard/tournament-leaderboard.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { PlayerSelfAssessmentComponent } from './components/player-self-assessment/player-self-assessment.component';
import { CreateMatchStatisticsComponent } from './components/match-statistics/match-statistics.component';
import { PlayerRatingComponent } from './components/player-rating/player-rating.component';
import { JerseyComponent } from './components/jersey/jersey.component';
import { NotificationComponent } from './components/notification/notification.component';
import { CreateTournamentComponent } from './components/create-tournament/create-tournament.component';

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'tactical-preparation', component: TacticalPreparationComponent },
  { path: 'tournament-leaderboard', component: TournamentLeaderboardComponent },
  { path: 'player-self-assessment', component: PlayerSelfAssessmentComponent },
  { path: 'create-player-rating', component: PlayerRatingComponent },
  { path: 'create-match-statistics', component: CreateMatchStatisticsComponent },
  { path: 'player-rating', component: PlayerRatingComponent },
  { path: 'jersey', component: JerseyComponent },
  { path: 'notifications', component: NotificationComponent },
  { path: 'create-tournament', component: CreateTournamentComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' }, // default route
  { path: '**', redirectTo: '/dashboard' } // wildcard route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
