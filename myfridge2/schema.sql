CREATE TABLE IF NOT EXISTS User (
  Id INT NOT NULL,
  Name VARCHAR(200) NULL,
  email VARCHAR(200) NULL,
  password VARCHAR(45) NULL,
  PRIMARY KEY (Id)
);


CREATE TABLE IF NOT EXISTS `Product` (
  `id` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Picture` VARCHAR(45) NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE IF NOT EXISTS `Fridge` (
  `Amount` FLOAT NULL,
  `userId` INT NULL,
  `productId` INT NULL,
  INDEX `fk_Fridge_2_idx` (`productId` ASC),
  INDEX `fk_Fridge_1_idx` (`userId` ASC),
  CONSTRAINT `fk_Fridge_1`
    FOREIGN KEY (`userId`)
    REFERENCES `User` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fridge_2`
    FOREIGN KEY (`productId`)
    REFERENCES `Product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS `Recipe` (
  `id` INT NOT NULL,
  `Name` VARCHAR(200) NULL,
  `Text` TEXT(1000) NULL,
  PRIMARY KEY (`id`)
);


CREATE TABLE IF NOT EXISTS `Ingredients` (
  `Amount` FLOAT NULL,
  `RecipeId` INT NULL,
  `productId` INT NULL,
  INDEX `fk_Fridge_2_idx` (`productId` ASC),
  INDEX `fk_Fridge_10_idx` (`RecipeId` ASC),
  CONSTRAINT `fk_Fridge_10`
    FOREIGN KEY (`RecipeId`)
    REFERENCES `Recipe` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Fridge_20`
    FOREIGN KEY (`productId`)
    REFERENCES `Product` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

