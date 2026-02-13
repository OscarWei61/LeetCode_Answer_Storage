CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.
	select distinct
        user_id
    from
        Purchases
    where
        amount >= minAmount
        and
        time_stamp >= startDate
        and
        time_stamp <= endDate
    order by
        user_id asc;
END