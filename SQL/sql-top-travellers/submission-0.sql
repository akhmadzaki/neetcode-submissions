-- Write your query below

select name, case when sum(distance) > 0 then sum(distance) else 0 end as travelled_distance from users u left join rides r on u.id=r.user_id
group by name order by travelled_distance desc, name asc