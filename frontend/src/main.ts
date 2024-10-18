// TODO
// import { enableProdMode } from '@angular/core';
// import { environment } from './environments/environment'; // Adjust the path as necessary
// if (environment.production) {
//   enableProdMode(); // Enable production mode if the environment is production
// }

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module'; // Adjust the path as necessary


// Bootstrap the root module
platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch(err => console.error(err));