SELECT MCDP_CD AS "진료과코드", COUNT(PT_NO) AS "5월예약건수"
FROM APPOINTMENT
-- [수정 1] 연도(2022)와 월(05)을 모두 체크해야 함!
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
-- [수정 2] 문제에서 요구한 정렬 조건 추가 (예약수 오름차순 -> 진료과코드 오름차순)
ORDER BY COUNT(PT_NO) ASC, MCDP_CD ASC;