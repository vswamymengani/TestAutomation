import pandas as pd
from openpyxl.workbook import Workbook
exl_data={"hospital_name":["Apollo","max","folio"],
          "claim_amt":"",
          "claim_status":["yes","in_progress","yes"]
        }
#write xl file
df=pd.DataFrame(exl_data)
df.to_excel("claim.xlsx",sheet_name="claim",index=False)
#read xl file
read_df=pd.read_excel("claim.xlsx",sheet_name="claim")
print(read_df)