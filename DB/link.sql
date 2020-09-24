
CREATE TABLE chat_bot.link
(
    id serial NOT NULL,
    home_page varchar(100) ,
    title_page  varchar(100) ,
    simple_title_page  varchar(100) ,
    url_page  varchar(100) ,
    CONSTRAINT link_pkey PRIMARY KEY (id)
)
