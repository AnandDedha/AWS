Select userid, name, gender, genderlooking, age,
       Case when lang_fr =True then 'French'
            when lang_en =True then 'English'
            when lang_de =True then 'German'
            when lang_it =True then 'Italian'
            when lang_es =True then 'Hindi'
            when lang_pt =True then 'Spanish'
           else "Language missing" end as Lang,
     lastonlinetime
from myDataSource


-- DDL table

CREATE  SCHEMA dating_app_schema;
CREATE TABLE dating_app_schema.cust_dim (
  userid varchar(25) not null, 
  name varchar(50) not null, 
  gender varchar(25)  not null,   
  genderlooking varchar(25)  not null,
  age int,
  Lang varchar(25)  not null,  
  lastonlinetime TIMESTAMP
   )


