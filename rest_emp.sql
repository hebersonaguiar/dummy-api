CREATE TABLE `rest_emp` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `address` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `rest_emp`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `rest_emp`
 MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;


 CREATE TABLE IF NOT EXISTS rest_emp (
	id INT AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=INNODB;