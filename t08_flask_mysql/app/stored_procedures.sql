CREATE SCHEMA  IF NOT EXISTS `iot_db`;
USE `iot_db`;


DELIMITER //

CREATE TRIGGER before_insert_photo_table
BEFORE INSERT ON photo
FOR EACH ROW
BEGIN
    DECLARE user_exist INT;

    SELECT COUNT(*) INTO user_exist FROM user WHERE user_id = NEW.user_id;

    IF user_exist = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'User record does not exist';
    END IF;
END;

//

DELIMITER ;

DELIMITER //
CREATE TRIGGER after_delete_min_row6
AFTER DELETE
ON role FOR EACH ROW
BEGIN
     IF(SELECT COUNT(*) FROM role ) < 3
     THEN  SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Delete error MIN cardinality';
END IF;
END//
DELIMITER ;
DELETE FROM role WHERE role_id=3;

DELIMITER //
CREATE TRIGGER validate_name
AFTER INSERT
ON user FOR EACH ROW
BEGIN
	DECLARE valid_name BOOLEAN;
    SET valid_name = NEW.name IN ('Svitlana', 'Petro', 'Olha', 'Taras');

    IF NOT valid_name THEN
        SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Username is not valid';

END IF;
END//
DELIMITER ;

DELIMITER //
CREATE TRIGGER reject_deleting
BEFORE DELETE
ON game FOR EACH ROW
BEGIN
      SIGNAL SQLSTATE '45000'
	  SET MESSAGE_TEXT = 'Username is not valid';
END //
DELIMITER ;


CREATE PROCEDURE insert_server_data(
    server_id_param INT,
    name_param VARCHAR(45),
    creation_date_param DATETIME
)
BEGIN
    INSERT INTO `server` (server_id, name, creation_date)
    VALUES (server_id_param, name_param, creation_date_param);
END//
DELIMITER ;

CALL insert_server_data(5, 'ServerName', '2023-01-01 15:06:00');

DELIMITER //
CREATE PROCEDURE insert_rows()
BEGIN
    DECLARE counter INT DEFAULT 1;
    DECLARE new_name VARCHAR(45);
    WHILE counter <= 10 DO
        SET new_name = CONCAT('noname', counter);
        INSERT INTO user (username) VALUES (new_name);
        SET counter = counter + 1;
    END WHILE;
END//
DELIMITER ;
CALL insert_rows;

DELIMITER //
CREATE FUNCTION find_value(table_name VARCHAR(45), column_name VARCHAR(45), operation_name VARCHAR(10))
RETURNS DECIMAL(18,2)
DETERMINISTIC READS SQL DATA
BEGIN
	 SET @result=0;
	 CASE operation_name
		  WHEN "MAX" THEN
				SELECT MAX(column_name) INTO @result FROM table_name;
		  WHEN "AVG" THEN
				SELECT AVG(column_name) INTO @result FROM table_name;
		  WHEN "MIN" THEN
				SELECT MIN(column_name) INTO @result FROM table_name;
		  WHEN "SUM" THEN
				SELECT SUM(column_name) INTO @result FROM table_name;
	  END CASE;

      RETURN @result;
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE calculate_statistics(IN table_name VARCHAR(45), IN column_name VARCHAR(45), IN operation_name VARCHAR(10), OUT result DECIMAL(18,2))

BEGIN
    SET result = find_value(table_name, column_name, operation_name);
END //

DELIMITER ;

CALL calculate_statistics('game','price','MIN',@result);

DELIMITER //
CREATE PROCEDURE InsertUserDataWithRole(
    IN p_email VARCHAR(45),
    IN p_username VARCHAR(45),
    IN p_about_user VARCHAR(100),
    IN p_in_discord DATETIME,
    IN p_game_id INT,
    IN p_role_name VARCHAR(45),
    IN p_role_description VARCHAR(200)
)
BEGIN
    DECLARE v_user_id INT;
    DECLARE v_role_id INT;

    INSERT INTO `user` (email, username, about_user, in_discord, game_id)
    VALUES (p_email, p_username, p_about_user, p_in_discord, p_game_id);

    SET v_user_id = LAST_INSERT_ID();

    INSERT INTO `role` (name, description)
    VALUES (p_role_name, p_role_description);

    SET v_role_id = LAST_INSERT_ID();

    INSERT INTO user_role (user_id, role_id)
    VALUES (v_user_id, v_role_id);
END //
DELIMITER ;
-- Cursor
DELIMITER //
CREATE PROCEDURE cursor_procedure()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE usernameDB CHAR(25);
    DECLARE counter INT DEFAULT 1;
	DECLARE num_of_tables INT;
    DECLARE my_cursor CURSOR FOR SELECT name FROM server;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;


    OPEN my_cursor;

    myLoop: LOOP
        FETCH my_cursor INTO usernameDB;
        IF done THEN
            LEAVE myLoop;
        END IF;

        SET @drop_query = CONCAT('DROP DATABASE IF EXISTS ', usernameDB, '');
        PREPARE drop_query FROM @drop_query;
        EXECUTE drop_query;
        DEALLOCATE PREPARE drop_query;

        SET @name_query = CONCAT('CREATE DATABASE IF NOT EXISTS ', usernameDB, '');
        PREPARE my_query FROM @name_query;
        EXECUTE my_query;
        DEALLOCATE PREPARE my_query;


        SET num_of_tables = FLOOR(RAND() * 9) + 1;
        SET counter = 1;


        WHILE counter <= num_of_tables DO
            SET @table_name = CONCAT(usernameDB, '_', counter);
            SET @query = CONCAT('CREATE TABLE IF NOT EXISTS ', usernameDB, '.', @table_name, ' (id INT, name VARCHAR(255));');
            PREPARE create_table_query FROM @query;
            EXECUTE create_table_query;
            DEALLOCATE PREPARE create_table_query;
            SET counter = counter + 1;
        END WHILE;
    END LOOP;

    CLOSE my_cursor;
END//
DELIMITER ;
CALL cursor_procedure();

DROP PROCEDURE IF EXISTS cursor_procedure;


