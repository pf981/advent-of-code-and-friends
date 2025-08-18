WITH letters AS (
    SELECT * FROM letters_a
    UNION ALL
    SELECT * FROM letters_b
),
chars AS (
    SELECT
        char(value) AS character,
        id
    FROM letters
    WHERE
        (
            (character BETWEEN 'A' AND 'Z' OR character BETWEEN 'a' AND 'z')
            OR (character IN (' ', '!', '"', '''', '(', ')', ',', '-', '.', ':', ';', '?'))
        )
    ORDER BY id
)
SELECT 
    group_concat(character, '') AS message
FROM chars;
