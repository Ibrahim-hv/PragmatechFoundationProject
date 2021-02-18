create table Şirkətlər(
    id integer primary key,
    s_ad varchar(50),
    ex_ad varchar(20),
    voen varchar(10),
    s_tel varchar(30),
    ex_tel varchar(30),
    unvan varchar(30)
);

-- CREATE DATA
insert into Kassalar(ad, kassa_ad, icaze)
values('Ibrahim', 'Kassa 1', 'true');

-- READ DATA
select * from Endirimlər;

-- UPDATE DATA


-- DELETE DATA
DELETE FROM Kassalar WHERE id=1;