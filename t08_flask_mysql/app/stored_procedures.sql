USE `iot_db`;
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
CALL insert_server_data(2, 'ServerName', '2023-01-01 15:06:00');

DELIMITER //
CREATE PROCEDURE insert_rows()
BEGIN
    DECLARE counter INT DEFAULT 1;
    DECLARE new_name VARCHAR(45);
    WHILE counter <= 10 DO
        SET new_name = CONCAT('Noname', counter);
        INSERT INTO user (username) VALUES (new_name);
        SET counter = counter + 1;
    END WHILE;
END//
DELIMITER ;
CALL insert_rows();


