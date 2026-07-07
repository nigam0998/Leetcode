WITH UserCategories AS (SELECT DISTINCT pp.user_id, pi.category FROM ProductPurchases pp JOIN ProductInfo pi ON pp.product_id = pi.product_id),

CategoryPairs AS (SELECT u1.user_id, LEAST(u1.category, u2.category) AS category1, GREATEST(u1.category, u2.category) AS category2 FROM UserCategories u1 JOIN UserCategories u2 ON u1.user_id = u2.user_id AND u1.category < u2.category)

SELECT category1, category2, COUNT(DISTINCT user_id) AS customer_count FROM CategoryPairs GROUP BY category1, category2 HAVING COUNT(DISTINCT user_id) >= 3 ORDER BY customer_count DESC, category1 ASC, category2 ASC;