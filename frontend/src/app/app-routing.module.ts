import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateMatchFactComponent } from './components/create-match-fact/create-match-fact.component';
import { CreatePlayerRatingComponent } from './components/create-player-rating/create-player-rating.component';
import { AuthGuard } from './services/auth.guard';

const routes: Routes = [
  { path: 'create-match-fact', component: CreateMatchFactComponent, canActivate: [AuthGuard] },
  { path: 'create-player-rating', component: CreatePlayerRatingComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
