--Postgres answers to the questions from https://www.jitbit.com/news/181-jitbits-sql-interview-questions/

--Question 1
--select e.nm from employees e 
--inner join employees b 
--on e.boss_id = b.id
--where e.salary > b.salary

--Question 2 # Ugly
--select * from employees e inner join
--(select dept_id, max(salary) salary from employees e group by dept_id) s
--on s.dept_id = e.dept_id and s.salary = e.salary

--Question 2 # Also Ugly
--select * from 
--(select row_number() over (partition by dept_id order by salary desc) as rn, nm, salary, dept_id 
--from employees) x
--where rn = 1

--Question 3
--select count(id), dept_id from employees group by dept_id having count(id) < 3

--Question 4
--select count(e.nm),d.nm from employees e full outer join departments d on d.id = e.dept_id
--group by d.nm

--Question 5
--select e.nm from employees e inner join
--employees b 
--on e.boss_id = b.id
--where e.dept_id <> b.dept_id

--Question 6
--select d.nm, coalesce(sum(salary),0) from departments d left join employees e on e.dept_id = d.id group by d.nm
