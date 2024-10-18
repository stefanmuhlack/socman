import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { PlayerRatingChartComponent } from './components/player-rating-chart/player-rating-chart.component';
import { ChartsModule } from 'ng2-charts';

@NgModule({
  declarations: [
    AppComponent,
    PlayerRatingChartComponent,
    // other components
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    // other modules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
