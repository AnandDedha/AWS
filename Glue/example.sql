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
