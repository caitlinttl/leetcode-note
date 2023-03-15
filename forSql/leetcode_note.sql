-- 1071. Greatest Common Divisor of Strings Easy---------------------------------------

Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255))
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255))
Truncate table Person
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen')
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob')
Truncate table Address
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York')
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California')

Input: 
Person table:
+----------+----------+-----------+
| personId | lastName | firstName |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+---------------+------------+
| addressId | personId | city          | state      |
+-----------+----------+---------------+------------+
| 1         | 2        | New York City | New York   |
| 2         | 3        | Leetcode      | California |
+-----------+----------+---------------+------------+
Output: 
+-----------+----------+---------------+----------+
| firstName | lastName | city          | state    |
+-----------+----------+---------------+----------+
| Allen     | Wang     | Null          | Null     |
| Bob       | Alice    | New York City | New York |
+-----------+----------+---------------+----------+

-- Answer:
SELECT lastName , firstName ,city , state FROM Person LEFT JOIN Address ON Person.personId = Address.personId
select firstName, lastName, city, state from person p left join address a on p.personId = a.personId;



-- 181. Employees Earning More Than Their Managers Easy---------------------------------------
Create table If Not Exists Employee (id int, name varchar(255), salary int, managerId int)
Truncate table Employee
insert into Employee (id, name, salary, managerId) values ('1', 'Joe', '70000', '3')
insert into Employee (id, name, salary, managerId) values ('2', 'Henry', '80000', '4')
insert into Employee (id, name, salary, managerId) values ('3', 'Sam', '60000', 'None')
insert into Employee (id, name, salary, managerId) values ('4', 'Max', '90000', 'None')

Input: 
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.

-- Answer:
select name as Employee from Employee e where managerId <> 'null' and salary > (select salary from Employee m where e.managerId = m.id); 
select name as Employee from Employee e where salary > (select salary from Employee m where e.managerId = m.id); 
select e.name Employee from Employee e JOIN Employee m on e.managerId = m.id where e.salary > m.salary;
-- this solution faster than above




-- 182. Duplicate Emails Easy---------------------------------------
Create table If Not Exists Person (id int, email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'a@b.com')
insert into Person (id, email) values ('2', 'c@d.com')
insert into Person (id, email) values ('3', 'a@b.com')


Input: 
Person table:
+----+---------+
| id | email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
Output: 
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Explanation: a@b.com is repeated two times.

-- Answer:
-- openbook
select email Email from Person group by email having count(email) > 1;


-- 183. Customers Who Never Order Easy---------------------------------------
Create table If Not Exists Customers (id int, name varchar(255))
Create table If Not Exists Orders (id int, customerId int)
Truncate table Customers
insert into Customers (id, name) values ('1', 'Joe')
insert into Customers (id, name) values ('2', 'Henry')
insert into Customers (id, name) values ('3', 'Sam')
insert into Customers (id, name) values ('4', 'Max')
Truncate table Orders
insert into Orders (id, customerId) values ('1', '3')
insert into Orders (id, customerId) values ('2', '1')

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

-- Answer:
select c.name Customers from Customers c where c.id not in (select customerId from Orders);
select c.name Customers from Customers c left join Orders o on c.id = o.customerId where o.customerId is null;

-- 196. Delete Duplicate Emails Easy---------------------------------------
Create table If Not Exists Person (Id int, Email varchar(255))
Truncate table Person
insert into Person (id, email) values ('1', 'john@example.com')
insert into Person (id, email) values ('2', 'bob@example.com')
insert into Person (id, email) values ('3', 'john@example.com')

Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.


-- Answer:
select * from Person where id in (select min(id) from Person group by email);
delete p1 from person p1, person p2 where p1.email = p2.email and p1.id > p2.id;

# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
with my_list as
    (select email, min(id) as to_keep from Person
    group by email)

    delete from Person 
    where id not in (select to_keep from my_list);


-- 197. Rising Temperature Easy---------------------------------------
Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

-- Answer:
-- openbook
SELECT w1.id from Weather w1, Weather w2 where dateDiff(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;

-- 511. Game Play Analysis I Easy---------------------------------------
Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+

-- Answer:
select player_id, min(event_date) as first_login from Activity group by player_id;

-- 584. Find Customer Referee Easy---------------------------------------
Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

-- Answer:
select name from Customer where referee_id <> 2 or referee_id is null;

-- 586. Customer Placing the Largest Number of Orders Easy---------------------------------------
Input: 
Orders table:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
Output: 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
Explanation: 
The customer with number 3 has two orders, which is greater than either customer 1 or 2 because each of them only has one order. 
So the result is customer_number 3.

-- Answer:
-- openbook
select customer_number from Orders group by customer_number order by count(order_number) desc limit 1;


-- 595. Big Countries Easy---------------------------------------
Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

-- Answer:
select name, population, area from World where area >= 3000000 or population >= 25000000;


-- 596. Classes More Than 5 Students Easy---------------------------------------
Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation: 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.

-- Answer:
select class from Courses group by class having count(class) >= 5;


-- 607. Sales Person Easy---------------------------------------
-- Answer:
select s.name from SalesPerson s 
where s.sales_id not in 
(select sales_id from Orders o, Company c where c.com_id = o.com_id and c.name = 'RED');


-- 620. Not Boring Movies Easy---------------------------------------
-- openbook
-- Answer:
select * from Cinema where id % 2 <> 0 and description <> 'boring' order by rating desc;
select * from Cinema where mod(id,2) = 1 and description <> 'boring' order by rating desc;


-- 627. Swap Salary Easy---------------------------------------
-- openbook
-- Answer:
update Salary set sex = if(sex = 'f', 'm', 'f');
update Salary set sex = case when sex = 'f' then 'm' else 'f' end;


-- 1050. Actors and Directors Who Cooperated At Least Three Times Easy---------------------------------------
-- Answer:
-- openbook
select actor_id, director_id from ActorDirector group by actor_id, director_id having count(timestamp) >= 3;


-- 1084. Sales Analysis III Easy---------------------------------------
-- openbook
-- # Wherever you are given a range, keep MIN() and MAX() in mind
-- TIP: 遇到Range的問題, 用group by 搭配 having min and max.
-- Answer:
select p.product_id, p.product_name from Product p 
left join Sales s on p.product_id = s.product_id
group by s.product_id having min(s.sale_date) >= '2019-01-01' and max(s.sale_date) <= '2019-03-31';


-- 1141. User Activity for the Past 30 Days I Easy---------------------------------------
-- openbook
-- TIP: count 裡面也可用 distinct
-- Answer:
select activity_date as day, count(distinct user_id) as active_users from Activity 
-- where datediff('2019-07-27',activity_date) <= 30 <<<<是錯的, 因為負值(比7/27之後的日期)也小於30
where datediff('2019-07-27',activity_date) between 0 and 29 -- 是29不是30, between本身是包含邊界的, 題目是27(包含)的30天
-- 如果是27(包含)的5天, 是27, 26, 25, 24, 23, 那麼是between 0 and 4(27-23),也就是(5-1), 也就是>22(不含),<=27(含)
group by activity_date;

select activity_date as day, count(distinct user_id) as active_users from Activity 
where (activity_date > "2019-06-27" AND activity_date <= "2019-07-27") 
group by activity_date;


-- 1148. Article Views I Easy---------------------------------------
-- Answer:
select distinct author_id as id from Views where author_id = viewer_id order by id asc;

-- 1179. Reformat Department Table Easy---------------------------------------
-- openbook
-- Answer:
select id, 
sum(IF(month = 'Jan', revenue, null)) as Jan_Revenue,
sum(IF(month = 'Feb', revenue, null)) as Feb_Revenue,
sum(IF(month = 'Mar', revenue, null)) as Mar_Revenue,
sum(IF(month = 'Apr', revenue, null)) as Apr_Revenue,
sum(IF(month = 'May', revenue, null)) as May_Revenue,
sum(IF(month = 'Jun', revenue, null)) as Jun_Revenue,
sum(IF(month = 'Jul', revenue, null)) as Jul_Revenue,
sum(IF(month = 'Aug', revenue, null)) as Aug_Revenue,
sum(IF(month = 'Sep', revenue, null)) as Sep_Revenue,
sum(IF(month = 'Oct', revenue, null)) as Oct_Revenue,
sum(IF(month = 'Nov', revenue, null)) as Nov_Revenue,
sum(IF(month = 'Dec', revenue, null)) as Dec_Revenue
from Department group by id



-- 1407. Top Travellers Easy---------------------------------------
-- openbook
-- 1. 判斷是否為空, 用 IFNULL
-- 2. 左邊資料都要有, 用left join
-- Answer:
select u.name, IFNULL(sum(r.distance), 0) travelled_distance from Users u 
left join Rides r on r.user_id = u.id 
group by r.user_id order by travelled_distance desc, name asc;



-- 1484. Group Sold Products By The Date Easy---------------------------------------
-- openbook
-- GROUP_CONCAT() 即可將多筆查詢結果串接合併為一筆
-- Answer:
select sell_date, count(distinct product) num_sold, 
group_concat(distinct product ORDER BY product separator ',') products
from Activities 
GROUP BY sell_date
ORDER BY sell_date asc;



-- 1527. Patients With a Condition Easy---------------------------------------
-- Answer:
SELECT patient_id, patient_name, conditions from Patients where conditions like 'DIAB1%' or conditions like '% DIAB1%';


-- 1581. Customer Who Visited but Did Not Make Any Transactions Easy---------------------------------------
-- Answer:
SELECT customer_id, count(customer_id) count_no_trans from Visits v 
LEFT JOIN Transactions t 
on v.visit_id = t.visit_id 
where v.visit_id not in (select visit_id from Transactions) -- where t.visit_id is NULL
GROUP BY customer_id;

-- 1587. Bank Account Summary II Easy---------------------------------------
-- Answer:
select name, sum(t.amount) balance from Users u
LEFT JOIN Transactions t
on u.account = t.account
GROUP BY u.account
having balance > 10000;


-- 1667. Fix Names in a Table Easy---------------------------------------
-- openbook
-- CONCAT, UPPER, LOWER, SUBST (LEFT, RIGHT)
-- Answer:
select user_id, 
CONCAT(UPPER(SUBSTR(name,1,1)), LOWER(SUBSTR(name,2))) as name 
CONCAT(UPPER(LEFT(name,1)), LOWER(RIGHT(name,LENGTH(name)-1))) as name 
from Users
order by user_id;


-- 1693. Daily Leads and Partners Easy---------------------------------------
-- Answer:
select date_id, make_name,
count(distinct lead_id) as unique_leads,
count(distinct partner_id) as unique_partners
from DailySales group by date_id, make_name;


-- 1729. Find Followers Count Easy---------------------------------------
-- Answer:
select user_id, count(follower_id) as followers_count
from Followers f GROUP BY user_id ORDER BY user_id


-- 1741. Find Total Time Spent by Each Employee Easy---------------------------------------
-- Answer:
select event_day as day, emp_id, sum(out_time - in_time) as total_time
from Employees GROUP BY event_day, emp_id;


-- 1757. Recyclable and Low Fat Products Easy---------------------------------------
-- Answer:
select product_id from Products 
where low_fats = 'Y' and recyclable = 'Y';


-- 1795. Rearrange Products Table Easy---------------------------------------
-- Answer:
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products WHERE store1 IS NOT NULL
UNION
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products WHERE store2 IS NOT NULL
UNION
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products WHERE store3 IS NOT NULL;


-- 1873. Calculate Special Bonus Easy---------------------------------------
-- Answer:
select employee_id, 
(case when (employee_id % 2 <> 0 and SUBSTR(name,1,1) <> 'M') then salary else 0 end) as bonus 
from Employees
order by employee_id; 

-- 1890. The Latest Login in 2020 Easy---------------------------------------
-- openbook
-- 先 where 再 group by !! 
-- 特定年份可以用YEAR(time_stamp)
-- Answer:
select user_id, max(time_stamp) as last_stamp
from Logins
where YEAR(time_stamp) = '2020'
-- where time_stamp like '2020%'
GROUP BY user_id;

-- 1965. Employees With Missing Information Easy---------------------------------------
-- openbook
-- Answer:
select e.employee_id from Employees e left join salaries s on e.employee_id = s.employee_id where s.salary is NULL
UNION
select s.employee_id from salaries s left join Employees e on e.employee_id = s.employee_id where e.name is NULL
ORDER BY employee_id;

select T.employee_id
from 
    (select * from Employees left JOIN Salaries USING(employee_id)
    UNION
    select * from Employees RIGHT JOIN Salaries USING(employee_id))
as T
where T.salary is null or T.name is NULL
ORDER BY employee_id;


-- 176. Second Highest Salary Medium---------------------------------------
-- openbook
-- limit 有兩個參數(省略第一個預設為0) [開始項] [數量]
-- Answer:
select IFNULL((select distinct salary from Employee order by salary desc limit 1,1),null) as SecondHighestSalary;
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from Employee);


-- 177. Nth Highest Salary Medium---------------------------------------
-- openbook
-- 設定參數用 SET
-- Answer:
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from Employee order by salary desc limit N, 1
      
  );
END


-- 178. Rank Scores Medium---------------------------------------
-- openbook
-- Answer:
select score, 
(select count(distinct score) from Scores where score >= s.score) as 'rank' 
from Scores s 
ORDER BY score desc;

-- 180. Consecutive Numbers Medium---------------------------------------
-- Answer:
select distinct num as ConsecutiveNums
from Logs L
where (num = (select num from Logs where id = (L.id)+1))
and (num = (select num from Logs where id = (L.id)+2));

-- 184. Department Highest Salary Medium---------------------------------------
-- openbook
-- 先 where 再 group by !! 
-- Answer:
select (d.name) as Department, (e.name) as Employee, e.salary as salary
from Employee e, Department d
where e.departmentId = d.id
and (departmentId, salary) in 
(select departmentId, max(salary) from Employee group by departmentId);

-- 608. Tree Node Medium---------------------------------------
-- Answer:
select id,
(case 
when p_id is null then 'Root' 
when (id in (select p_id from Tree)) then 'Inner' 
else 'Leaf' end) 
as 'type'
from Tree;

-- 626. Exchange Seats Medium---------------------------------------
-- lead and lag 取得後一筆(lead)與前一筆(lag)，搭配over (order by xxx)使用
-- Answer:
select s.id,
(case 
when s.id % 2 = 1 and s.id = (select max(id) from Seat) then student
when s.id % 2 = 1 then (select student from Seat where id = s.id + 1)
when s.id % 2 = 0 then (select student from Seat where id = s.id - 1) end) 
as student
from Seat s;

select id,
(case
when id % 2 = 1 and id = (select max(id) from Seat) then student
when id % 2 = 1 then (lead(student,1) over (ORDER BY id asc))
when id % 2 = 0 then (lag(student,1) over (ORDER BY id asc))
end) as student
from Seat;

-- 1158. Market Analysis I Medium---------------------------------------
-- openbook
-- where會把結果全過濾，而join...and會返回null不會過濾掉原表結果
-- 最後group by 要用原表的條件
-- Answer:
select u.user_id as buyer_id, join_date,
IFNULL(count(order_id),0) as orders_in_2019 -- 可以不用IFNULL
from Users u
left join Orders o
on u.user_id = o.buyer_id
AND year(o.order_date) = '2019'
group by u.user_id;

/* Why there is a difference between using AND YEAR(order_date) and WHERE YEAR(order_date) ??
If you use where you are filtering the result after the left join, 
in this case all the orders not in 2019 will be EXCLUDED. 
The multiple conditions in left join is saying , 
if I can not find matched id and satisfy YEAR(order_date) = '2019', 
then the query result for that row will still be kept ,
 but its joined columns will be null. */


-- 1393. Capital Gain/Loss Medium---------------------------------------
-- openbook
-- Answer:
select stock_name, sum(
    CASE 
        WHEN  operation = 'buy' THEN -price  
        ELSE  price
    END
) as capital_gain_loss
from Stocks
GROUP BY stock_name;

-- SUM(IF(operation='Buy',-price,price))
