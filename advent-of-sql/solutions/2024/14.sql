WITH Records AS (
    SELECT
        sr.record_id,
        sr.record_date,
        json_extract(r.value, '$.receipt_id') AS receipt_id,
        json_extract(r.value, '$.garment') AS garment,
        json_extract(r.value, '$.color') AS color,
        json_extract(r.value, '$.cost') AS cost,
        json_extract(r.value, '$.drop_off') AS drop_off,
        json_extract(r.value, '$.pickup') AS pickup
    FROM SantaRecords sr
    JOIN json_each(sr.cleaning_receipts) AS r
)
SELECT MAX(drop_off) AS last_drop_off
FROM Records
WHERE
    garment = 'suit'
    AND color = 'green';