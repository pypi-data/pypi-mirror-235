import sys
import json
import logging


def parse_input(sysargs: list, plugin_params: dict) -> dict:
    # # Verify plugin_params are provided
    # if "required" or "optional" not in plugin_params.keys():
    #     logging.error(f"must include input params dictionary with keys `required` and `optional`")
    #     sys.exit(1)

    # Verify user input parameters are consistent with plugin_params
    if len(sysargs) != 2:
        logging.error(f"must include input params dictionary with keys `required` and `optional`")
        sys.exit(1)

    # Read parameters in to dict to verify and pass to the plugin for execution
    try:
        params = json.loads(sysargs[1])
    except Exception as e:
        logging.error(str(e))
        sys.exit(1)

    # Verify parameters
    missing_inputs = []

    for p in plugin_params["required"]:
        if p not in params.keys():
            missing_inputs.append(p)

    if len(missing_inputs) > 0:
        logging.error(f"Verify all inputs are correct. Required: {plugin_params}, Provided: {params}")
        sys.exit(1)

    logging.info("successfully verified input parameters")
    return params


def plugin_logger():
    logging.root.handlers = []
    return logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%dT%H:%M:%SZ",
        format="""{"time": "%(asctime)s" , "level": "%(levelname)s", "msg": "%(message)s"}""",
        handlers=[logging.StreamHandler()],
    )


def print_results(results: dict):
    print(json.dumps({"plugin_results": results}))
