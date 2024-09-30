downloadPlayerData() {
  this.playerRatingService.exportPlayerData().subscribe(blob => {
    const a = document.createElement('a');
    const objectUrl = URL.createObjectURL(blob);
    a.href = objectUrl;
    a.download = 'players.csv';
    a.click();
    URL.revokeObjectURL(objectUrl);
  });
}
