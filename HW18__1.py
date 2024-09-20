update orders set total_price = (select sum(p.price * po.amount)
from products_orders po join products p
on po.product_id = p.product_id
group by po.order_id
having orders.order_id = po.order_id)
#############################################################
select o.order_id, o.date_time, p.name from orders o  join products_orders po
on o.order_id = po.order_id
join products p on p.product_id = po.product_id order by o.order_id
######################################################
update orders set total_price = (select sum(p.price * po.amount)
from products_orders po join products p
on po.product_id = p.product_id
group by po.order_id
having orders.order_id = po.order_id)
############################################
select o.order_id, o.total_price from orders o
where o.total_price = (select max(o.total_price) from orders o)
union
select o.order_id, o.total_price from orders o
where o.total_price = (select min(o.total_price) from orders o)
union
select o.order_id, o.total_price from orders o
where o.total_price = (select avg(o.total_price) from orders o)
###########################################

SELECT customer_name, counter
FROM (
    SELECT o.customer_name, COUNT(*) AS counter
    FROM orders o
    JOIN products_orders po
    ON o.order_id = po.order_id
    GROUP BY o.customer_name
) AS order_count
ORDER BY counter DESC
LIMIT 1;

#v
SELECT o.customer_name, COUNT(*) AS counter
FROM orders o
JOIN products_orders po
ON o.order_id = po.order_id
GROUP BY o.customer_name
HAVING COUNT(*) =
(SELECT MAX(counter) AS max_count
    FROM (
        SELECT COUNT(*) AS counter
        FROM orders o
        JOIN products_orders po
        ON o.order_id = po.order_id
        GROUP BY o.customer_name
    ))
##############################################################
# vii
select p.product_id, p.name, count(*) as counter
from products p join products_orders po
on p.product_id = po.product_id
group by p.product_id
having count(*) =
(select max(counter) from
(SELECT COUNT(*) AS counter
        FROM products p
        JOIN products_orders po
        ON p.product_id = po.product_id
        GROUP BY p.product_id
    ))
select p.product_id, p.name, count(*) as counter
from products p join products_orders po
on p.product_id = po.product_id
group by p.product_id
having count(*) =
(select min(counter) from
(SELECT COUNT(*) AS counter
        FROM products p
        JOIN products_orders po
        ON p.product_id = po.product_id
        GROUP BY p.product_id
    ))
select p.product_id, p.name, count(*) as counter
from products p join products_orders po
on p.product_id = po.product_id
group by p.product_id
having count(*) =
(select avg(counter) from
(SELECT COUNT(*) AS counter
        FROM products p
        JOIN products_orders po
        ON p.product_id = po.product_id
        GROUP BY p.product_id
    ))

##########################################
# VIII
select p.product_id, p.name, c.category_id, c.name, count(*) as counter
from products p join products_orders po
on p.product_id = po.product_id
join category c on c.category_id = p.category_id
group by (p.product_id, c.category_id)
having count(*) =
(select max(counter) from
(SELECT COUNT(*) AS counter
        FROM products p
        JOIN products_orders po
        ON p.product_id = po.product_id
        GROUP BY p.product_id, c.category_id
    ))
###########################
# ix(BONUS)
select p.product_id, count(*) as counter
	from
	products p join products_orders po
	on p.product_id = po.product_id
	join orders o
	on po.order_id = o.order_id
	group by p.product_id
	having count(*) =
	(select max(cnt) as counter from
	(select count(*) cnt from
	products p join  products_orders po
	on p.product_id = po.product_id
	join orders o
	on o.order_id = po.order_id
	group by p.product_id))
	order by p.product_id


