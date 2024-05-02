with transformed_europe_sales_data as (
    select Country
    , item_type
    , order_date
    , units_sold
    , unit_price
    , unit_cost
    , total_revenue
    , total_cost
    , total_profit
from (
    select Country
        , item_type
        , order_date
        , units_sold
        , unit_price
        , unit_cost
        , sum(total_revenue) as total_revenue
        , sum(total_cost) as total_cost
        , sum(total_profit) as total_profit
    from  {{ ref('stg_europe') }}
    group by 1,2,3,4,5,6
    order by 1 asc
)
)
select *
from transformed_europe_sales_data