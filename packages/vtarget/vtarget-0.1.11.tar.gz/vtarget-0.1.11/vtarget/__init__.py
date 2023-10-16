import os
import uuid


def run_flow(path: str) -> None:
    import gc
    import json

    from vtarget.dataprep.builder import Builder
    from vtarget.handlers.bug_handler import bug_handler
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

    nodes = {
        node_key: {
            port_name: cache_handler.cache[flow_id][node_key]["pout"][port_name]
            for port_name in cache_handler.cache[flow_id][node_key]["pout"]
        }
        for node_key in cache_handler.cache[flow_id]
        if "type" in cache_handler.cache[flow_id][node_key]
        and cache_handler.cache[flow_id][node_key]["type"] == "V_Output"
    }

    cache_handler.reset(flow_id)

    gc.collect()

    for bug in bug_handler.bug:
        node_key = bug["node_key"] if "node_key" in bug else None
        if node_key:
            level = bug["level"] if "level" in bug else "info"
            msg = bug["msg"] if "msg" in bug else None
            if msg:
                print(f"[{level}] {msg}")

    return nodes