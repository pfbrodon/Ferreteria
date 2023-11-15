CREATE TABLE buloneria.stockFerreteria (
	codigo	INT NOT NULL,
	categoria	VARCHAR(50) NOT NULL,
	descripcion	VARCHAR(50) NOT NULL,
	cantidad	INT NOT NULL,
	precioUnit	DECIMAL(10, 2) NOT NULL,
	precioVPublico	DECIMAL(10, 2) NOT NULL
);
COMMIT;
