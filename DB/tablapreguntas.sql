
CREATE TABLE chat_bot.question (
	id serial NOT NULL,
	question varchar(100) NULL,
	simple_question varchar(100) NULL,
	answer varchar(100) NULL,
	CONSTRAINT question_pkey PRIMARY KEY (id)
);

insert into chat_bot.question values (1,'indique su nombre', 'nombre','Jhon Torres')


select * from chat_bot.question