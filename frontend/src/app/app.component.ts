import { Component, OnInit } from '@angular/core';
import { LocalStorageService } from './local-storage.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})

export class AppComponent {
  isDarkMode = false;

  toggleDarkMode() {
    this.isDarkMode = !this.isDarkMode;
    const body = document.getElementsByTagName('body')[0];
    if (this.isDarkMode) {
      body.classList.add('dark-mode');
    } else {
      body.classList.remove('dark-mode');
    }
  }
}
