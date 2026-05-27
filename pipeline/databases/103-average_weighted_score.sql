--ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_weighted_score = (
        SELECT SUM(c.score * p.weight) / SUM(p.weight)
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id
    )
    WHERE id = user_id;
END //

DELIMITER ;
