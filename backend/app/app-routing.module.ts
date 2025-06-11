import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { PlayerStatsViewComponent } from './components/player-stats-view/player-stats-view.component';
import { TeamStatsViewComponent } from './components/team-stats-view/team-stats-view.component';
import { MatchFactsTableComponent } from './components/match-facts-table/match-facts-table.component';
import { TrackingHeatmapComponent } from './components/tracking-heatmap/tracking-heatmap.component';
import { AdminImportLogComponent } from './components/admin-import-log/admin-import-log.component';

const routes: Routes = [
  { path: 'player-stats', component: PlayerStatsViewComponent },
  { path: 'team-stats', component: TeamStatsViewComponent },
  { path: 'match-facts', component: MatchFactsTableComponent },
  { path: 'tracking', component: TrackingHeatmapComponent },
  { path: 'import-log', component: AdminImportLogComponent },
  { path: '', redirectTo: 'player-stats', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
