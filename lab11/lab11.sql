.read sp20data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students 
    WHERE smallest > 2
    ORDER BY smallest
    LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color
    FROM students as s1, students as s2
    WHERE s1.pet = s2.pet AND s1.song = s2.song
      AND s1.time < s2.time;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here


CREATE TABLE stacks AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
