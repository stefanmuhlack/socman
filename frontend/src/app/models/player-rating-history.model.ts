export interface PlayerRatingHistory {
  id: number;
  player_id: number;
  metrics: { [key: string]: number };
  timestamp: string;
}
