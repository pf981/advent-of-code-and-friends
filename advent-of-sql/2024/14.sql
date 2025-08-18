WITH Records AS (
    SELECT
  		record_id,
  		record_date,
  		receipt_id,
  		garment,
  		color,
  		cost,
  		drop_off,
  		pickup
    FROM
        SantaRecords,
        jsonb_to_recordset(cleaning_receipts) AS (
          "receipt_id" text,
          "garment" text,
          "color" text,
          "cost" float,
          "drop_off" date,
          "pickup" date
        )
)
SELECT MAX(drop_off)
FROM Records
WHERE
	garment = 'suit'
	AND color = 'green'
;
