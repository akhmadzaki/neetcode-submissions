-- Write your query below

select c.customer_id, c.customer_name from customers c join orders o on c.customer_id = o.customer_id
group by c.customer_id
HAVING COUNT(*) FILTER (WHERE o.product_name = 'A') > 0
   AND COUNT(*) FILTER (WHERE o.product_name = 'B') > 0
   AND COUNT(*) FILTER (WHERE o.product_name = 'C') = 0
order by c.customer_name;
