import os
import uuid


def run_flow(path: str) -> None:
    import gc
    import json

    from vtarget.dataprep.builder import Builder
    from vtarget.handlers.cache_handler import cache_handler

    content = open(path, "r")
    data = json.loads(content.read())
    builder = Builder()
    builder.init_pipeline()
    flow_id = str(uuid.uuid4())
    builder.analyzer(
        data["model"],
        True,
        flow_id,
        os.path.basename(path),
        False,
        False,
    )
    del builder.pipeline
    gc.collect()
    return cache_handler.cache[flow_id]


if __name__ == "__main__":
    print(run_flow("C:\\Users\\aflor\\Downloads\\model_crec_proy_cat_nf.json"))
