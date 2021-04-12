# Installation rapide de l'application

Créer un environnement virtuel "auth" :

```python
python3 -m venv auth
```

Activer l'environnement virtuel :

- sous bash

```bash
source auth/bin/activate
```

- sous windows


```powershell
auth\Scripts\activate
```

Lancer l'application :

```python
python3 -m flask run
```



## Mysql workbench

Créer la base de donnée dans MySql workbench avec la query suivante : 

```sql
CREATE DATABASE IF NOT EXISTS `geeklogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `geeklogin`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `password`varchar(255) NOT NULL,
    `email`varchar(100) NOT NULL,
    primary key (`id`)
    ) ENGINE=InnoDB auto_increment=2 DEFAULT CHARSET=utf8;
```

