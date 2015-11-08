
SELECT * FROM famous_people  WHERE nationality = 'USA';

SELECT count(*) FROM famous_people  WHERE nationality = 'USA';

SELECT sum(estimated_iq_score) FROM famous_people  WHERE nationality = 'Germany';

SELECT avg(estimated_iq_score) FROM famous_people  WHERE occupation = 'politician';

SELECT occupation, avg(estimated_iq_score) e_avg_iq FROM famous_people
GROUP BY occupation
ORDER BY e_avg_iq DESC;
