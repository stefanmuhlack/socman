import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
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
    ChartsModule,
    // other modules
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
