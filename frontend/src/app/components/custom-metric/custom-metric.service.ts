import { Component } from '@angular/core';
import { CustomMetricService } from '../../services/custom-metric.service';

@Component({
  selector: 'app-create-custom-metric',
  templateUrl: './create-custom-metric.component.html',
})
export class CreateCustomMetricComponent {
  newMetric = {
    name: '',
    description: '',
  };

  constructor(private customMetricService: CustomMetricService) {}

  createMetric() {
    this.customMetricService.createCustomMetric(this.newMetric).subscribe(() => {
      // Handle success
    }, error => {
      // Handle error
    });
  }
}
