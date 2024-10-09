export interface PlayerRating {
  id?: number;
  player_id: number;
  coach_id: number;
  metrics: any; // TODO: add interface for metrics
  ball_manipulation: number;
  kicking_ability: number;
  passing_ability: number;
  duel_tackling: number;
  field_coverage: number;
  blocking_ability: number;
  game_strategy: number;
  playmaking_risk: number;
  rating_date: Date;
}
