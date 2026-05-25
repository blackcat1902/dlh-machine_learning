
DELIMITER $$


BEGIN
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user
    SELECT AVG(score)
    INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = IFNULL(avg_score, 0)
    WHERE id = user_id;
END $$

DELIMITER ;
