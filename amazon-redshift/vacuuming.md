## Examples of Vacuum

#### Syntax      
      VACUUM [ FULL | SORT ONLY | DELETE ONLY | REINDEX | RECLUSTER ] [ [ table_name ] [ TO threshold PERCENT ] [ BOOST ] ]

#### Examples

Reclaim space and database and re-sort rows in all tables based on the default 95 percent vacuum threshold.
     
     vacuum;

Always reclaim space and re-sort rows in the SALES table.

     vacuum sales to 100 percent;

Re-sort rows in the SALES table only if fewer than 75 percent of rows are already sorted.

      vacuum sort only sales to 75 percent;

Reclaim space in the SALES table such that at least 75 percent of the remaining rows aren't marked for deletion following the vacuum.

      vacuum delete only sales to 75 percent;
