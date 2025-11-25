-- 코드를 입력하세요
SELECT c.CAR_TYPE, count(c.car_id) as CARS
from car_rental_company_car c
WHERE c.options LIKE '%통풍시트%'
   OR c.options LIKE '%열선시트%'
   OR c.options LIKE '%가죽시트%'
group by c.car_type
order by c.car_type