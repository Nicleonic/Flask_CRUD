ALTER TABLE `promotion` ADD FOREIGN KEY (`fk_dep`) REFERENCES `departement`(`id_departement`) ON DELETE CASCADE ON UPDATE CASCADE;



ALTER TABLE `etudiant` ADD FOREIGN KEY (`fk_promotion`) REFERENCES `promotion`(`id_prom`) ON DELETE CASCADE ON UPDATE CASCADE;