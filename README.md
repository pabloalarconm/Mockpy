## Welcome to mockpy

Dataframe editor for tidy data management and reusability

### Functions:

column_editor(dict) Use a Python dict() to edit Columns names, like this:
  ```python3
{'Prev_column_name':'New_name','Prev_column_name_2':'New_name_2'}
  
```
content_replacement(json,innewplace) Use JSON structure for applying replacements at Dataframe information, like this:
  ```python3
{
    'Column_name_X': {
        'Prev_valueA': 'New_valueA',
        'Prev_valueB': 'New_valueB'
        }, 
    'Column_name_Y': {
        'Prev_valueN': 'New_valueN'
        }
}
  
```
innewplace parameter must be added:
True: If you want to add changes to a duplicated column
False: If you want to apply these changes to original column

```python3
import mockpy.mockpy as m
import json
import pandas as pd
data_trial= pd.ExcelFile("/home/yourroot/dataframe.xlsx")

df=data_trial.parse()

dict_columns={'Identifier': 'ID', 'Diagnosis': 'Disease'}
json_replace='{"Gender":{"Female":"Mujer","Male":"Hombre"},"Disease":{"Adiposis dolorosa":"Adiposis_dolorosa"}}'
json_test=json.loads(json_replace)


test=m.mockpy(df)
test1=test.column_editor(dict_columns)
test2=test.content_replacement(json_test,innewplace=False)
test1
test2




```
