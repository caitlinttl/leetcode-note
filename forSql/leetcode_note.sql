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


-- num_title Easy Medium---------------------------------------
-- Answer:

-- num_title Easy Medium---------------------------------------
-- Answer:

-- num_title Easy Medium---------------------------------------
-- Answer:

-- num_title Easy Medium---------------------------------------
-- Answer:

-- num_title Easy Medium---------------------------------------
-- Answer:

