CREATE TABLE chat_bot.rasa_template_item (
	id serial NOT NULL,
	item_type varchar(100) NULL,
	item_value varchar(100) NULL,
	tem_id bigint NOT NULL,
	CONSTRAINT item_pkey PRIMARY KEY (id),
	constraint item_tem_id FOREIGN KEY (tem_id) REFERENCES chat_bot.rasa_template (id)
);
