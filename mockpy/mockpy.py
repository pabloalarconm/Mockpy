import sys

class mockpy(object):

    def __init__(self,dataset):
        self.dataset = dataset
        if dataset.empty:
            sys.exit("""
            Dataset MUST be added as parameter to continue... 
            """)
        else:
            print("""
            Welcome to MockPy:

            # Functions:

            ## column_editor(dict) Use a Python dict() to edit Columns names, like this:
            {'Prev_column_name':'New_name','Prev_column_name_2':'New_name_2'}
            
            ## content_replacement(json) Use JSON structure for applying replacements at Dataframe information, like this:
            {
                'Column_name_X': {
                    'Prev_valueA': 'New_valueA',
                    'Prev_valueB': 'New_valueB'
                    }, 
                'Column_name_Y': {
                    'Prev_valueN': 'New_valueN'
                    }
            }
            
            
            """)

    
    # For column name renaming:
    def column_editor(self,dict_editor):
        self.dict_editor=dict_editor
        if not type(self.dict_editor) == dict:
            sys.exit("""
            dict used as input configuration is not valid:
            Input configuration object MUST be a Python dictionary like this:
            
            {'Prev_column_name':'New_name','Prev_column_name_2':'New_name_2'}
            
            """)
        self.dataset.rename(columns=self.dict_editor, inplace=True)
        return(self.dataset)
    
    # Takes a JSON and makes changes on the dataframe based on JSON information.
    def content_replacement(self,json_editor,innewplace):
        self.json_editor=json_editor
        if not type(self.json_editor) == dict:
            sys.exit("""
            JSON used as input configuration is not valid:
            JSON/dict input parameter MUST be a JSON like this:
            
            {
                'Column_name_X': {
                    'Prev_valueA': 'New_valueA',
                    'Prev_valueB': 'New_valueB'
                    }, 
                'Column_name_Y': {
                    'Prev_valueN': 'New_valueN'
                    }
            }
            
            """)
            
        for column in self.dataset:
            for jkey,jvalue in self.json_editor.items():
                for jval in jvalue.items():
                    if innewplace == True:
                        self.dataset[jkey+"new"] = self.dataset[column]
                        self.dataset[jkey+"new"] = self.dataset[jkey+"new"].replace(jval[0],jval[1])
                    elif innewplace == False:
                        self.dataset[column]= self.dataset[column].replace(jval[0],jval[1])
                    else:
                        sys.exit("""
                        innewplace parameter MUST be added:
                        True: If you want to add changes to a duplicated column
                        False: If you want to apply these changes to original column
                        """)

        return(self.dataset)
        
        