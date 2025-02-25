BEGIN TRANSACTION;
CREATE TABLE `departments` (
            `id` INTEGER NOT NULL,
            `name` TEXT NOT NULL UNIQUE,
            PRIMARY KEY(`id` AUTOINCREMENT)
        );
CREATE TABLE `employees` (
                `id` INTEGER NOT NULL,
                `name` TEXT NOT NULL,
                `age` INTEGER NOT NULL,
                `department` TEXT NOT NULL, `department_id` INTEGER REFERENCES `departments` (`id`),
                PRIMARY KEY (`id` AUTOINCREMENT)
            );
INSERT INTO "employees" VALUES(2,'Maria',60,'IT',NULL);
INSERT INTO "employees" VALUES(3,'Sarah',100,'Marketing',NULL);
INSERT INTO "employees" VALUES(4,'Susan',29,'Marketing',NULL);
INSERT INTO "employees" VALUES(5,'Paul',40,'Sales',NULL);
INSERT INTO "employees" VALUES(6,'Daniel',31,'Support',NULL);
INSERT INTO "employees" VALUES(7,'John',32,'Marketing',NULL);
INSERT INTO "employees" VALUES(8,'Sarah',28,'Management',NULL);
INSERT INTO "employees" VALUES(9,'Claude',36,'IT',NULL);
INSERT INTO "employees" VALUES(10,'Michael',34,'Sales',0);
CREATE INDEX `idx_name` ON `employees`(`name`);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('employees',10);
COMMIT;
