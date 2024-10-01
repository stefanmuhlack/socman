import { Component } from '@angular/core';

@Component({
  selector: 'app-tactical-preparation',
  templateUrl: './tactical-preparation.component.html',
})
export class TacticalPreparationComponent {
  players = [
    { id: 1, name: 'Torwart', position: 'TW' },
    { id: 2, name: 'Linker Verteidiger', position: 'LV' },
    { id: 3, name: 'Innenverteidiger Links', position: 'IVL' },
    { id: 4, name: 'Innenverteidiger Zentral', position: 'IVZ' },
    { id: 5, name: 'Innenverteidiger Rechtsr', position: 'IVR' },
    { id: 6, name: 'Innenverteidiger Links', position: 'IVL' },
    { id: 7, name: 'Rechter Verteidiger', position: 'RV' },
    { id: 8, name: 'Defensives linkes äußeres Mittelfeld', position: 'DLM' },
    { id: 9, name: 'Defensives Mittelfeld Links', position: 'DML' },
    { id: 10, name: 'Defensives Mittelfeld Zentral', position: 'DMZ' },
    { id: 11, name: 'Defensives Mittelfeld Rechts', position: 'DMR' },
    { id: 12, name: 'Defensives rechtes äußeres Mittelfeld', position: 'DRM' },
    { id: 13, name: 'Linkes Mittelfeld', position: 'LM' },
    { id: 14, name: 'Halb Links', position: 'HL' },
    { id: 15, name: 'Mittelfeld Zentral', position: 'MZ' },
    { id: 16, name: 'Halb Rechts', position: 'HR' },
    { id: 17, name: 'Rechtes Mittelfeld', position: 'RM' },
    { id: 18, name: 'Offensives Linkes Mittelfeld', position: 'OLM' },
    { id: 19, name: 'Offensives Halblinkes Mittelfeld', position: 'OHL' },
    { id: 20, name: 'Zentral Offensiv', position: 'ZO' },
    { id: 20, name: 'Offensives Halbrechtes Mittelfeld', position: 'OHR' },
    { id: 21, name: 'Offensives Rechtes Mittelfeld', position: 'ORM' },
    { id: 22, name: 'Hängende Spitze', position: 'HST' },
    { id: 23, name: 'Links Außen', position: 'LA' },
    { id: 24, name: 'Sturm Links', position: 'STL' },
    { id: 25, name: 'Sturm Zentral', position: 'STZ' },
    { id: 26, name: 'Sturm Rechts', position: 'STR' },
    { id: 27, name: ' Rechts Außen', position: 'RA' },
    
    // Add more players with positions
  ];

  onPlayerPositionChange(event: any) {
    const { player, target } = event;
    console.log('Player moved:', player);
    console.log('New target position:', target.position);
  }

  saveFormation() {
  const formationData = {
    formationName: this.formation.name,
    players: this.players.map(p => ({
      player_id: p.id,
      position: p.position
    }))
  };

  this.tacticalService.saveFormation(formationData).subscribe(response => {
    alert('Formation saved successfully!');
  });
}



createFormation() {
    const formationData = {
        name: this.formation.name,
        players: this.players.map(p => ({ player_id: p.id, position: p.position }))
    };
    
    this.tacticalService.createFormation(formationData).subscribe(response => {
        alert('Formation saved successfully!');
    });
}
