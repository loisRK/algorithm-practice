-- 코드를 입력하세요
SELECT HISTORY_ID,
       CAR_ID,
       DATE_FORMAT(start_date, "%Y-%m-%d") as start_date,
       DATE_FORMAT(end_date, "%Y-%m-%d") as end_date,
       if(DATEDIFF(end_date,start_date) >= 29, '장기 대여', '단기 대여') as rent_type
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
where date_format(start_date,"%Y-%m") LIKE '2022-09' 
ORDER BY 1 DESC;       