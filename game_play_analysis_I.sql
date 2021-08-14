/*
https://leetcode.com/problems/game-play-analysis-i/
GIVEN
INPUT
Activity: Table
    column
        player_id : int
        device_id : int
        event_data : date
        games_played : int
    (player_id, event_data) is the primary key of this table
    shows the activity of players of some gae
    each row is a record of a player who logged in and played a number of games
        could be 0
    before logging out on some day using some device
OUTPUT
report the first login data for each player
    sort by player_id, then event_date
# ORDER BY player_id, event_date;
*/
SELECT
    player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
