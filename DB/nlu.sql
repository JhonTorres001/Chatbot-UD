-- Drop table

-- DROP TABLE public.nlu;

CREATE TABLE public.nlu (
	id serial NOT NULL,
	nlu_type varchar(100) NULL,
	nlu_name varchar(100) NULL,
	value varchar[] NULL,
	CONSTRAINT nlu_pkey PRIMARY KEY (id)
);
