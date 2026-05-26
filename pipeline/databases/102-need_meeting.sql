--create a view 
CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students AS new_meeting
WHERE score < 80 
  AND (
        last_meeting IS NULL 
        OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
      );
