export interface PlayerRating {
  id?: number;
  player_id: number;
  coach_id: number;
  metrics: any; // TODO: add interface for metrics
  ballManipulation: number;
  kickingAbility: number;
  passingAbility: number;
  duelTackling: number;
  fieldCoverage: number;
  blockingAbility: number;
  gameStrategy: number;
  playmakingRisk: number;
  rating_date: Date;
}
