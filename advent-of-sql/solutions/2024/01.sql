WITH child_wishes AS (
    SELECT
        wl.list_id,
        wl.child_id,
        wl.submitted_date,
        json_extract(wl.wishes, '$.first_choice') AS first_choice,
        json_extract(wl.wishes, '$.second_choice') AS second_choice,
        json_extract(wl.wishes, '$.colors[0]') AS favorite_color,
        (
          SELECT COUNT(*) 
          FROM json_each(json_extract(wl.wishes, '$.colors'))
        ) AS color_count
    FROM wish_lists wl
)
SELECT
    c.name,
    cw.first_choice AS primary_wish,
    cw.second_choice AS backup_wish,
    cw.favorite_color,
    cw.color_count,
    CASE
        WHEN toy1.difficulty_to_make = 1 THEN 'Simple Gift'
        WHEN toy1.difficulty_to_make = 2 THEN 'Moderate Gift'
        ELSE 'Complex Gift'
    END AS gift_complexity,
    CASE toy1.category
        WHEN 'outdoor' THEN 'Outside Workshop'
        WHEN 'educational' THEN 'Learning Workshop'
        ELSE 'General Workshop'
    END AS workshop_assignment
FROM children c
JOIN child_wishes cw USING (child_id)
JOIN toy_catalogue toy1 ON toy1.toy_name = cw.first_choice
ORDER BY c.name, primary_wish
LIMIT 5;