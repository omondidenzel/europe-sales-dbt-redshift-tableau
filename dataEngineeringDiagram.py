from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.programming.language import Python
from diagrams.aws.storage import S3
from diagrams.aws.analytics import Redshift

with Diagram('Europe Sales ELT', show=True): 
     csv_file = Custom('CSV File', '/Users/omondidenzel/Desktop/DENZEL/DATA-ENGINEERING/DE/icons/csv_logo.svg')    
     python_logo = Python('Python')
     dbt =  Custom('dbt', '/Users/omondidenzel/Desktop/DENZEL/DATA-ENGINEERING/DE/icons/dbt_logo.svg')
     tableau = Custom('Tableau', '/Users/omondidenzel/Desktop/DENZEL/DATA-ENGINEERING/DE/icons/tableau_logo.svg')

     with Cluster('AWS Cluster'):      
          s3_bucket = S3('S3 Bucket')
          redshift = Redshift('Redshift')
          python_logo >> s3_bucket >> redshift 
          

     csv_file >> python_logo 
     redshift >> tableau
     redshift >> dbt 
     dbt >> redshift
    
    
