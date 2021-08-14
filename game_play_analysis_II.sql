/*
https://leetcode.com/problems/game-play-analysis-ii/
GIVEN
INPUT
Table : Activity

OUTPUT
    reports the device that is first logged in for each player
*/

SELECT
    Activity.player_id, Activity.device_id
FROM (
    SELECT
        player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS LoginTable
INNER JOIN Activity
ON Activity.player_id = LoginTable.player_id AND
Activity.event_date = LoginTable.first_login;
