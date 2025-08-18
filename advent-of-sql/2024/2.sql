WITH letters AS (
  	SELECT * FROM letters_a
  	UNION ALL SELECT * FROM letters_b
),
chars AS (
    SELECT
        CHR(value) AS character
    FROM letters
    WHERE
        CHR(value) ~ '[[:alpha:]]'
        OR CHR(value) IN (' ', '!', '"', '''', '(', ')', ',', '-', '.', ':', ';', '?')
    ORDER BY id
)
SELECT 
	STRING_AGG(character, '') AS message
FROM chars
;
