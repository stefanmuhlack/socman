import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { provideCharts, withDefaultRegisterables } from 'ng2-charts';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';
import { DashboardComponent } from './components/dashboard/dashboard.component';

@NgModule({
  declarations: [
    ...,
    DashboardComponent
  ],
})

@NgModule({
  declarations: [
    AppComponent,
    // other components
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    // other modules
  ],
  providers: [provideCharts(withDefaultRegisterables()),provideHttpClient(withInterceptorsFromDi())],
  bootstrap: [AppComponent]
})
export class AppModule { }
