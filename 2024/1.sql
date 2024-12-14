WITH child_wishes AS (
    SELECT
  		list_id,
  		child_id,
  		submitted_date,
  		first_choice,
  		second_choice,
  		colors[1] AS favorite_color,
  		ARRAY_LENGTH(colors, 1) AS color_count
    FROM
        wish_lists,
        json_to_record(wishes) AS (
          "first_choice" text,
          "second_choice" text,
          "colors" text[]
        )
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
FROM
	children c
	JOIN child_wishes cw USING (child_id)
	JOIN toy_catalogue toy1 ON toy1.toy_name = cw.first_choice
ORDER BY c.name
LIMIT 5
;
