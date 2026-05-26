--creates a view need_meeting that lists all students
SELECT score,last_meeting FROM  students AS new_meeting 
WHERE score<80 and (last_meeting IS  NULL  OR  last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));