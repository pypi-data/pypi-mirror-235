
import os
import csv
from typing import List, Tuple

from dftools.core.database.query_result import QueryExecResults
from dftools.events import log_event
from dftools.events.events import CSVFileWriteSuccessful

def write_script_exec_results_to_csv(script_results : List[Tuple[str, QueryExecResults]], file_path : str
        , delimiter : str = ';', newline : str = '\n', quotechar : str = '"') -> None:
    with open(file_path, 'w', newline=newline) as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter, quotechar=quotechar)
        writer.writerow(['Script Name', 'Script Status', 'Query Name', 'Query', 'Query Status', 'Execution Message', 'Start Tst', 'End Tst'])
        for script_result in script_results:
            script_name = os.path.basename(script_result[0])
            query_exec_result = script_result[1]
            for query_exec_result_csv_row in query_exec_result.get_csv_rows():
                csv_row = [script_name, query_exec_result.get_status()]
                csv_row.extend(query_exec_result_csv_row)
                writer.writerow(csv_row)
    log_event(None, CSVFileWriteSuccessful(file_path=file_path, object_type_name="ScriptExecResults"))
