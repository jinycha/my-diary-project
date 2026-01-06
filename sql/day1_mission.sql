

create table diary (
	id int auto_increment PRIMARY key,
	date DATE not null,
	weather VARCHAR(50),
	content TEXT
);

insert into diary (date, weather, content)
values ('2026-01-05', '맑음', '오늘부터 SQL 공부를 시작했다. 생각보다 재미있다.');

insert into diary (date, weather, content)
values ('2026-01-04','비', '여러모로 정상적으로 지내는 것은 허상이다.');


select * from diary;

select * from diary where weather = '비';

update diary 
set weather = '흐림'
where date = '2026-01-05';

select * from diary where date = '2026-01-05';


delete from diary 
where date = '2026-01-05';

INSERT INTO diary (date, weather, content)
VALUES ('2025-12-30', '맑음', '얼마 안 남은 20살에 감흥이 있을까');

INSERT INTO diary (date, weather, content)
VALUES ('2025-12-31', '비', '순간은 광활해 공허하고 그의 집합은 순식간이다.');

insert into diary (date, weather, content)
values ('2026-01-01', '흐림', '21살이 되었고 낡은 기분을 느꼈다');

insert into diary (date, weather, content)
values ('2026-01-02', '비', '비가 왔다는 것은 거짓말이야 그럼에도 보이고 싶은 마음.');

insert into diary (date,  weather, content)
values ('2026-01-03', '맑음', '다들 몇 군데씩 허름한 채로 어른이 되는 것!');

select * from diary where weather = '비';

-- 1. 중복된 것 중, 앞에 있는 번호(1번, 6번)를 지웁니다.
DELETE FROM diary WHERE id = 1;
DELETE FROM diary WHERE id = 6;

-- 2. 잘 지워졌는지 전체 목록을 다시 확인합니다.
SELECT * FROM diary;

update diary 
set content = '다들 몇 군데씩 허름한 채로 어른이 되는 것! iykyk'
where date = '2026-01-03'

select * from diary;