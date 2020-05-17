INSERT INTO capture_adm.roles (id, name, description) VALUES (1, 'Admin', 'Administrator');
INSERT INTO capture_adm.roles (id, name, description) VALUES (2, 'Developer', 'User Developer');
INSERT INTO capture_adm.roles (id, name, description) VALUES (3, 'Seller', 'User can sell and view');
INSERT INTO capture_adm.roles (id, name, description) VALUES (4, 'Viewer', 'User only can view');

INSERT INTO capture_adm.categories (id, name, description) VALUES (1, 'Nature', 'Nature photos');
INSERT INTO capture_adm.categories (id, name, description) VALUES (2, 'City', 'City photos');
INSERT INTO capture_adm.categories (id, name, description) VALUES (3, 'Night', 'Night photos');
INSERT INTO capture_adm.categories (id, name, description) VALUES (4, 'Portrait', 'Portrait photos');

INSERT INTO capture_adm.users (id, public_id, first_name, last_name, password, email, profile_image, birth_date, created_date, role_id, is_active) VALUES (1, '7db5a3f1-88d6-4618-b829-bd4ddadb92da', 'One', 'single', '$pbkdf2-sha512$25000$aQ1BSOk9h/CeEyLEGKNUKg$eDNh7Mvp7pxsDk.NrThO4po4gxPnABJjmDZ52kpUFw9CGDdUEZoXqMYASmVX.8fZNk17z7QV8RbzIGwhPK8tLw', 'one@gmail.com', 'default.jpg', '1992-04-13 00:00:00', '2020-04-25 18:31:28.081527', 1,false);
INSERT INTO capture_adm.users (id, public_id, first_name, last_name, password, email, profile_image, birth_date, created_date, role_id, is_active) VALUES (2, 'a6964989-e121-4db3-a651-a4350693d461', 'Two', 'single', '$pbkdf2-sha512$25000$EaIUonSuFeL8HwNgrBVCyA$lrfY.QcCNMGASAZsAWbE752azZC95su3xZQKNbnrZtoHYID2YgGclmqhezocC5iAu3ezudGCF9IKvwdhT.LrlA', 'two@gmail.com', 'default.jpg', '1992-08-15 00:00:00', '2020-04-25 18:31:28.108527', 2,true);
INSERT INTO capture_adm.users (id, public_id, first_name, last_name, password, email, profile_image, birth_date, created_date, role_id, is_active) VALUES (3, 'd18100b4-57fb-4efb-be1e-9fdfc1e20886', 'Three', 'single', '$pbkdf2-sha512$25000$T0lJidE6B8CY0/q/976XUg$aJjefX/3p.lL80Mq7UXFV2jeO1ExaBfsBo7p06Hc9BQNnnXxoXmAvc8upDSCT2ClhXhrF9AimIz5h3QCNUDB2Q', 'three@gmail.com', 'default.jpg', '1998-01-22 00:00:00', '2020-04-25 18:31:28.133556', 3, true);
INSERT INTO capture_adm.users (id, public_id, first_name, last_name, password, email, profile_image, birth_date, created_date, role_id, is_active) VALUES (4, 'ad47fdad-76ad-401d-8d28-1867de93339b', 'Four', 'single', '$pbkdf2-sha512$25000$B8C4t5byPkdoTan1/n/vPQ$zj.Txxu6EOmFr9VrFuI.ppPV7pucUCL.MVH7y3IP9c9Mn.8eIup.1gdyJOh1OJegDATHnqb04BollId4N0kSyg', 'four@gmail.com', 'default.jpg', '1993-09-19 00:00:00', '2020-04-25 18:31:28.157524', 3,true);

INSERT INTO capture_adm.products (id, name, description, price, user_id, category_id, exclusivity) VALUES (1,'Naturescape','My photo about nature',19.90,1,1,false);
INSERT INTO capture_adm.products (id, name, description, price, user_id, category_id, exclusivity) VALUES (2,'Urban city','My photo about a city',30,2,2,true);
INSERT INTO capture_adm.products (id, name, description, price, user_id, category_id, exclusivity) VALUES (3,'Human Eyes','My photo about a girls eyes',40,3,4,false);


commit;