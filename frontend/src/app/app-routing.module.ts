import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PlayerRatingChartComponent } from './components/player-rating-chart/player-rating-chart.component';

const routes: Routes = [
  { path: 'player-rating/:playerId', component: PlayerRatingChartComponent },
  // other routes
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
