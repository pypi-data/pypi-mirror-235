from qctrlworkflowclient.router.api import DecodedResult


def metadata_formatter(input_: DecodedResult) -> DecodedResult:
    """
    Insert `action_id` to the `metadata` key of the result.

    Parameters
    ----------
    input_ : DecodedResult
        The result from the workflow functions.

    Returns
    -------
    DecodedResult
        The reformatted result.
    """
    result = input_.decoded
    assert isinstance(result, dict)
    if result.get("metadata") is None:
        result["metadata"] = {}
    result["metadata"].update({"action_id": input_.action_id})
    return input_


def async_result_formatter(input_: DecodedResult) -> dict:
    """
    Format the response result before updating it in the async result dictionary.

    Parameters
    ----------
    input_ : DecodedResult
        The result from the workflow functions.

    Returns
    -------
    dict
        The reformatted result.
    """
    result = metadata_formatter(input_)
    return result.decoded


def metadata_local_formatter(input_: dict) -> dict:
    """
    Fill action_id key as None in local mode.

    Parameters
    ----------
    input_ : dict
        Result from running workflow functions locally.

    Returns
    -------
    dict
        Formatted result.
    """
    if input_.get("metadata") is None:
        input_["metadata"] = {}
    input_["metadata"]["action_id"] = None
    return input_
