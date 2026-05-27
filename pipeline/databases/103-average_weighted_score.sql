--ComputeAverageScoreForUse



DELIMITER $$

BEGIN
    UPDATE users
    SET average_score = (
        SELECT IFNULL(
            SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0),
            0
        )
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id
    )
    WHERE id = user_id;
END $$

DELIMITER ;
