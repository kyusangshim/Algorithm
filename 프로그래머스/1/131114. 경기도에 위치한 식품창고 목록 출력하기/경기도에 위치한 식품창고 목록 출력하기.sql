-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') as FREEZER_YN
from food_warehouse
# where substring(warehouse_name, 2, 5) = '경기'
where warehouse_name like '%경기%'
order by warehouse_id
