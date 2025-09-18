-- create database 
create database analytics;

-- create groups
create group data_engineers;
create group data_analysts;

-- create user
create user denzel_de
    password '123456abc..'
    in group data_engineers;

-- assign create rights to data_engineers group for analytics database
grant create on database analytics to group data_engineers;

-- check if denzel_de has read permission if you see data the access worked
select *
from  sample_data_dev.tickit.category
limit 10;

--- R1m7Xs6#O1bnyhoP
-- create schema in analytics
create schema sales_dwh; 

-- copy europe table in sales to analytics table
create table analytics.sales_dwh.europe as (
select Region
    , Country
    , "Item Type" as item_type
    , "Sales Channel" as sales_channel
    , "Order Priority" as order_priority
    , "Order Date" as order_date
    , "Units Sold" as units_sold
    , "Unit Price" as unit_price
    , "Unit Cost" as unit_cost
    , "Total Revenue" as total_revenue
    , "Total Cost" as total_cost
    , "Total Profit" as total_profit
from (
    select *
    from sales.public.europe
)
)

-- Notes: Dive into big data
    -- Orchestration 
    -- Databricks/Azure data - Spark e.t.c.
    -- 