import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerRatingChartComponent } from './components/player-rating-chart/player-rating-chart.component';

const routes: Routes = [
  { path: 'player-rating/:playerId', component: PlayerRatingChartComponent },
  // other routes
];

const routes: Routes = [
  { path: 'dashboard', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: 'player-rating', loadChildren: () => import('./player-rating/player-rating.module').then(m => m.PlayerRatingModule) },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
