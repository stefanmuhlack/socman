import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateMatchFactComponent } from './components/create-match-fact/create-match-fact.component';
import { CreatePlayerRatingComponent } from './components/create-player-rating/create-player-rating.component';

const routes: Routes = [
  { path: 'create-match-fact', component: CreateMatchFactComponent },
  { path: 'create-player-rating', component: CreatePlayerRatingComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
