# database qa

## rising temperature
> days hotter than their previous day
```sql
SELECT w1.id
FROM Weather AS w1 , Weather AS w2
WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate , w2.recordDate) = 1
```

- faster solution
> Usage of EXISTS
> The EXISTS clause is generally efficient for checking the existence of rows because **it stops processing as soon as it finds a match. It doesn't need to retrieve all rows that satisfy the condition**; it just needs to confirm at least one exists. Dont have any expensive clause
> In this query we don't have any **expensive clause** like **JOIN, GROUP BY, IN, NOT IN. or implicit CROSS JOIN like multiple FROM t AS t1, t AS t2**.
```sql
SELECT current_day.id
FROM Weather AS current_day
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE current_day.temperature > yesterday.temperature
    AND current_day.recordDate = yesterday.recordDate + 1
);
```

## one with most friend
> table
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+

```sql
select id, sum(countx) as num
from
(SELECT requester_id as id, count(*) as countx
from RequestAccepted
group by requester_id
UNION ALL
SELECT accepter_id as id, count(*) as countx
from RequestAccepted
group by accepter_id) AS accepter_and_reciever
group by id
order by num desc
limit 1
```
- official solution
```sql
WITH all_ids AS (
   SELECT requester_id AS id 
   FROM RequestAccepted
   UNION ALL
   SELECT accepter_id AS id
   FROM RequestAccepted)
SELECT id, 
   COUNT(id) AS num
FROM all_ids
GROUP BY id
ORDER BY COUNT(id) DESC
LIMIT 1
```
