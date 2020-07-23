from os import path 
import re
import numpy as np 
import pandas as pd
import sys 
 
class EclipseFileParser:
    
    @staticmethod 
    def PetrelEclipseKeywords_to_pandas( file_name :str  )->pd.DataFrame:
        """
        Converts to a pandas dataframe the data stored as a Petrel file.
        Note that the file format includes * and other characters that have 
        a special meaning. These are supported. 

        Comments are assumed to start with --

        Exceptions: 
        Does not throw but returns early if the error is that the file cannot be opened
        Other errors raise the default exception 
        
        """
        data = {}
        has_numbers = EclipseFileParser._has_numbers;
        process_numbers = EclipseFileParser._process_numbers
        try:
            f = open(file_name, 'rt')

        except OSError:
            print ("Could not open/read file:", file_name)
            return None;#sys.exit()

        line  = f.readline()
        prop_name = ""

        total_parsed = 1
        while line:      
            #this is a property change 
            if "--" in line and ":" in line and "property" in line.lower():
                prop_name = line.strip().split(sep = ':')[1].strip()     
                data[prop_name] = [] 
                print( prop_name, end=', ' )
                total_parsed += 1
                if total_parsed %10 == True: 
                    print(); 

            elif  not("--" in line) and  has_numbers(line) == True:
                w = process_numbers(line)
                data[prop_name].extend( w )

            #note that scattered words in the file or those with -- but no new prop block are ignored
            line = f.readline()

        f.close() 

        return pd.DataFrame( data );

    
    @staticmethod 
    def _has_numbers(s: str)->bool:
        """
        Returns true of there are numbers in the string
        """
        return bool(re.search(r'\d', s))

    @staticmethod 
    def _process_numbers(line : str ):
        """
        Called by PetrelEclipseKeywords_to_pandas
        """
        line = line.replace('/','').replace('\\','').replace('\n','').split(sep=' ')  
        words = list(filter(None, line))    
        l = [] 
        for word in words:
            if '*' in word:
                times = int(word.split('*')[0])
                value = float(word.split('*')[1])
                l += times * [value]
            else:        

                l.append( float( word ))

        return l; 
    

    


def harmonize_names(data_raw:pd.DataFrame):
    date = ', timestep'
    print( "Processsing");
    for orig_column_name in data_raw.columns:

        column_name = orig_column_name
        print(".",end=' ');
        if 'VCOARSE' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('VCOARSE','VC')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name


        if 'YOUNGMOD' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('YOUNGMOD','YM')
            data_raw.rename(columns={column_name: new_name},inplace=True)     
            column_name = new_name

        if 'DENSITY' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('DENSITY','DENS')
            data_raw.rename(columns={column_name: new_name},inplace=True)      
            column_name = new_name

        if 'POISSONR' in column_name:
            #print('Processing ', column_name)   
            new_name = column_name.replace('POISSONR','PR')
            data_raw.rename(columns={column_name: new_name},inplace=True)   
            column_name = new_name

        if 'EFFSTR' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('EFFSTR','EFF')
            data_raw.rename(columns={column_name: new_name},inplace=True)   
            column_name = new_name

        if 'STRAIN' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('STRAIN','STRN')
            data_raw.rename(columns={column_name: new_name},inplace=True)   
            column_name = new_name

        if 'PRESSURE' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('PRESSURE','PPR')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name

        if 'INDEX_I' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('INDEX_I','I_FINE')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name  

        if 'INDEX_J' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('INDEX_J','J_FINE')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name  

        if 'INDEX_K' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('INDEX_K','K_FINE')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name     


        if 'VFINE' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('VFINE','FINE')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name   

        if 'POSX' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('POSX','X')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name   

        if 'POSY' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('POSY','Y')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name   

        if 'POSZ' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('POSZ','Z')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name     

        if 'DELTA' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('DELTA','D')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name     

        if 'Smooth' in column_name:
            #print('Processing ', column_name)
            new_name = column_name.replace('Smooth','SM_')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name    

        if date in column_name:
            new_name = column_name.replace(date,'')
            data_raw.rename(columns={column_name: new_name},inplace=True)
            column_name = new_name   

    print('done');

def pd_to_petrel_points( df, file_name, columns = []):
    """
    This is obsoleted. It was used to export as x,y,z points a data frame to then 
    load the points as a point-set in Petrel. This is not used anymore. 
    """
    print('pd_to_petrel_points');
    tmp =df[ columns ]
    print('Exporting rows ', len(tmp))
    tmp.to_csv(file_name, sep=' ', index = False)
    print('done')
    
    



