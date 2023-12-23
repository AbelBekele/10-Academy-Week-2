import pandas as pd
from logger import Logger
import sys
from datetime import datetime
class DataExtractor():
    
    def __init__(self)->None:
        try:
            self.logger=Logger().get_app_logger()
            self.logger.info('Data extractor object Initialized')
        except:
            pass
    
    def get_columns_and_rows(self,file_path)->tuple:
        try:
            with open(f'../data/{file_path}','r') as f:
                lines=f.readlines()

            columns=lines[0].replace('\n','').split(';')
            data=lines[0:40]
            return columns,data
        except Exception as e:
            # the try excepts here are for the airflow
            try:
                self.logger.error(f"Failed to read data: {e}")
            except:
                pass
            sys.exit(1)
    
    def chunk_list(self,list,chunk_size,default_first_val=None)->list:
        chunked_list=[]
        for i in range(0, len(list), chunk_size):
            if default_first_val:
                values=[default_first_val]
                values.extend(list[i:i+chunk_size])
                chunked_list.append(values)
            else:
                chunked_list.append(list[i:i+chunk_size])

        return chunked_list

    def prepare_data_for_pandas(self,columns,all_data,id_prefix)->tuple:
        try:
            traffic_cols=columns[:4]
            traffic_rows=[]

            timed_automobile_cols=['track_id']+columns[4:]
            timed_automobile_rows=[]

            for row in all_data:
                try:
                    items=row.replace('\n','').split(';')
                    items[0]=f"{id_prefix}_{items[0]}"
                    traffic_rows.append(items[:4])
                    timed_automobile_rows.extend(self.chunk_list(items[4:],6,items[0]))
                except Exception as e:
                    # the try excepts here are for the airflow
                    try:
                        self.logger.error(f"Failed preparing data for pands at row {row}: {e}")
                    except:
                        pass
            
            return (traffic_cols,traffic_rows),(timed_automobile_cols,timed_automobile_rows)
        except Exception as e:
            # the try excepts here are for the airflow
            try:
                self.logger.error(f"Failed to prepare data for pandas: {e}")
            except:
                pass
    
    def prepare_data_frame(self,traffic_data:tuple,timed_automobile_data:tuple):

        try:
            traffic_cols,traffic_rows=traffic_data
            timed_automobile_cols,timed_automobile_rows=timed_automobile_data

            traffic_data=pd.DataFrame(columns=traffic_cols,data=traffic_rows)
            timed_automobile_data=pd.DataFrame(columns=timed_automobile_cols,data=timed_automobile_rows)

            return traffic_data,timed_automobile_data

        except Exception as e:
            # the try excepts here are for the airflow
            try:
                self.logger.error(f"Failed to prepare data frame: {e}")
            except:
                pass

    def extract_data(self,file_name:str,return_json=False)->pd.DataFrame:
        try:
            # set the day and time as unique identifier
            id_prefix= f"{file_name.split('.')[0]}"
            columns,all_data=self.get_columns_and_rows(file_path=file_name)
            traffic_data, timed_automobile_data=self.prepare_data_for_pandas(columns=columns,all_data=all_data,id_prefix=id_prefix)
            if not return_json:
                return self.prepare_data_frame(traffic_data,timed_automobile_data)
            
            tr,vh= self.prepare_data_frame(traffic_data,timed_automobile_data)
            
            tr_file_name= str(datetime.today()).replace(' ','_')+"traffic.json"
            vh_file_name= str(datetime.today()).replace(' ','_')+"automobile_data.json"

            tr.to_json(f'../temp/{tr_file_name}',orient='records')
            vh.to_json(f'../temp/{vh_file_name}',orient='records')

            return tr_file_name,vh_file_name
        except Exception as e:
            print(e)
            try:
                self.logger.error(f"Failed to extract data: {e}")
            except:
                pass
    def separate_data(self,file_name:str,chunk_size:int = 100):
        pass