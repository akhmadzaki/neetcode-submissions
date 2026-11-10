-- Write your query below

with ranked_score as (
    select student_id, exam_id, score,
    rank() over(partition by student_id order by score desc, exam_id asc) as rank_num
    from exam_results
)
select student_id,exam_id, score
from ranked_score where rank_num = 1
order by student_id asc;


