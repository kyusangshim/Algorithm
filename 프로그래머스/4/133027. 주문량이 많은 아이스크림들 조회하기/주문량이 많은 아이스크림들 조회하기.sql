-- 코드를 입력하세요
# SELECT *
# from first_half f
# # join july j on f.flavor = j.flavor 
# order by f.total_order
# limit 3

# select j.flavor, sum(j.total_order) as total_sum
# from july j
# group by j.flavor

# select *
# from july j


SELECT f.flavor
from first_half f
join 
(select j.FLAVOR, sum(j.total_order) as TOTAL_ORDER
    from july j
    group by j.flavor
) s on f.flavor = s.flavor
group by f.flavor
order by sum(f.total_order) + sum(s.TOTAL_ORDER) DESC
limit 3