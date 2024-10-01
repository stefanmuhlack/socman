createFormation() {
    const formationData = {
        name: this.formation.name,
        players: this.players.map(p => ({ player_id: p.id, position: p.position }))
    };
    
    this.tacticalService.createFormation(formationData).subscribe(response => {
        alert('Formation saved successfully!');
    });
}
