INSERT INTO iot_db.client_type(id, type)
VALUES
(1, 'customer'), (2, 'staff'), (3, 'manager'), (4, 'friend');

INSERT INTO iot_db.client (name, number, client_type_id)
VALUES
('Pavelchak Andrii', 10023,  4),
('Veres Zenovii', 10026, 1),
('Yatsuk Yurii', 10030, 1),
('Samotyi Volodymyr', 20011, 2),
('Shevchenko Petro', 30028, 3);



INSERT INTO game (game_id, name, release_date, price)
VALUES

    (6, 'Mafia', '2021-07-06', 34),
    (7, 'UnoBot', '2022-06-04', 44),
    (8, 'Epic RPG', '2016-12-12', 34),
    (9, 'PokéTwo', '2015-09-04', 112),
    (10, 'Dank Memer', '2020-12-20', 2323);
