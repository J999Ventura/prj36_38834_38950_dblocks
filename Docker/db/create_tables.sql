CREATE TABLE roles(
	id int PRIMARY KEY,
	name VARCHAR (20) NOT NULL UNIQUE,
	description VARCHAR (100) NOT NULL
);

CREATE TABLE users(
	id serial PRIMARY KEY,
	public_id VARCHAR(50) NOT NULL UNIQUE,
	first_name VARCHAR (50) NOT NULL,
	last_name  VARCHAR (50) NOT NULL,
	email VARCHAR (50) UNIQUE NOT NULL,
	role_id int NOT NULL,
	birth_date date NOT NULL,
	created_date TIMESTAMP NOT NULL,
	last_login TIMESTAMP,
	FOREIGN KEY (role_id) references roles(id) ON DELETE CASCADE ON UPDATE CASCADE	  
);

CREATE TABLE users_details(
	user_id int,
	profile_photo VARCHAR (100),
	address varchar (100),
	country varchar (50),
	phone_number varchar (15) UNIQUE,
	primary key (user_id),
	FOREIGN KEY (user_id) references users(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE categories(
	id serial PRIMARY KEY,
	name VARCHAR (20) UNIQUE NOT NULL,
	description VARCHAR (100) NOT NULL
);

CREATE TABLE tags(
	name varchar(100) PRIMARY KEY,
	description varchar (150)
);

CREATE TABLE products(
	id serial PRIMARY KEY,
	user_id int NOT NULL,
	name VARCHAR (50) NOT NULL,
	description  VARCHAR (100) NOT NULL,
	image VARCHAR (50) NOT NULL UNIQUE, --para este caso e com marca de agua
	price date NOT NULL,
	category_id int NOT NULL,
	FOREIGN KEY (user_id) references users(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (category_id) references categories(id) ON DELETE CASCADE ON UPDATE CASCADE
);

--tabela que muda consoante o negocio, tem um trigger para preencher esta tabela quando se cria um produto e se insere na tabela products
CREATE TABLE products_details(
	product_id int,
	download_photo varchar (50) UNIQUE NOT NULL,
	exclusivity Boolean NOT NULL,
	primary key (product_id),
	FOREIGN KEY (product_id) references products(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE tags_products( --antes de inserir aqui tem que inserir primeiro a tag
	product_id int,
	tag_name varchar(100),
	primary key (product_id,tag_name),
	FOREIGN KEY (product_id) references products(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (tag_name) references tags(name) ON DELETE CASCADE ON UPDATE CASCADE	
);

CREATE TABLE users_products_favorites(
	user_id int,
	product_id int,
	primary key (user_id, product_id),
	FOREIGN KEY (user_id) references users(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) references products(id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- perguntar ao prof se devia haver so uma tabela os duas (compras ou vendas)
--so insere aqui quando o pagamento for concluido
CREATE TABLE transactions(
	id serial, --devia ser este?
	user_buyer_id int NOT NULL,
	user_seller_id int NOT NULL,
	product_id int NOT NULL,
	transaction_type VARCHAR(1) NOT NULL,
	price number NOT NULL,
	transaction_date date NOT NULL,
	payment_method int NOT NULL,
	PRIMARY KEY (id) --sera esta chave suficiente ?
	FOREIGN KEY (user_buyer_id) references users(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (user_seller_id) references users(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (product_id) references products(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (transaction_type) references transactions_type_ref_data(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (payment_method) references payment_methods_ref_data(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE transactions_type_ref_data(
	id serial,
	type varchar (20) NOT NULL UNIQUE,
	description (100),
	PRIMARY KEY (id)
)

CREATE TABLE payment_methods_ref_data(
	id serial,
	method varchar (50) NOT NULL UNIQUE,
	description varchar (100),
	PRIMARY KEY (id)
);
