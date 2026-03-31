CREATE OR REPLACE FUNCTION get_user_name_or_phone_number_by_pattern(p text):
RETURNS TABLE(id INT, first_name TEXT, second_name TEXT, phone_number TEXT UNIQUE) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook2 WHERE first_name ILIKE '%' || p || '%'
    OR second_name ILIKE '%' || p || '%'
    OR phone_number ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION show_with_pagination(limit_val INT, offset_val INT)
RETURNS TABLE(id, first_name, second_name, phone_number)
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook2
    ORDER BY id
    WHERE LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;