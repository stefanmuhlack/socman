import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerRatingChartComponent } from './components/player-rating-chart/player-rating-chart.component';

const routes: Routes = [
  { path: 'dashboard', loadChildren: () => import('./components/dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: 'player-ratings', loadChildren: () => import('./components/player-rating/player-rating.module').then(m => m.PlayerRatingModule) },
  { path: 'tournament-leaderboard', loadChildren: () => import('./components/tournament-leaderboard/tournament-leaderboard.module').then(m => m.TournamentLeaderboardModule) },
  { path: 'match-statistics', loadChildren: () => import('./components/match-statistics/match-statistics.module').then(m => m.MatchStatisticsModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
