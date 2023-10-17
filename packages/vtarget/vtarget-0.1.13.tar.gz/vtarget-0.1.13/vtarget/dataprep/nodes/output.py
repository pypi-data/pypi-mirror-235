import os

import pandas as pd

from vtarget.handlers.bug_handler import bug_handler
from vtarget.handlers.script_handler import script_handler
from vtarget.utils import normpath


class Output:
    def exec(self, flow_id, node_key, pin, settings):
        script_handler.script.append("\n# OUPUT")
        output_format: str = settings["format"] or "csv"
        output_name: str = settings["name"] if "name" in settings else "output"
        output_path: str = settings["path"] if "path" in settings else ""
        encoding: str = settings["encoding"] or "UTF-8"
        # print(columns, order)
        df: pd.DataFrame = pin["In"].copy()
        try:
            if output_format == "excel":
                file_path = output_path + os.path.sep + f"{output_name}.xlsx"
                file_path = normpath(file_path)
                df.to_excel(
                    file_path,
                    index=False,
                    encoding=encoding,
                )
                script_handler.script.append(
                    f"df.to_excel('{file_path}', index= False, encoding={encoding})"
                )
            else:
                file_path = output_path + os.path.sep + f"{output_name}.csv"
                file_path = normpath(file_path)
                df.to_csv(
                    file_path,
                    encoding=encoding,
                    index=False,
                )
                script_handler.script.append(
                    f"df.to_csv('{file_path}', index= False, encoding={encoding})"
                )

        except Exception as e:
            print("Error (output): ", e)
            msg = f"(output) No fue posible aplicar el output: {str(e)}"
            return bug_handler.default_on_error(flow_id, node_key, msg, str(e))

        return df
