import json
from Week6.src.tools.tools import call_tool

def route_llm_output(llm_text):
    try:
        data = json.loads(llm_text)
        if not isinstance(data, dict):
            return llm_text, False
        func = data.get("function")
        args = data.get("arguments", {})
        if not func:
            return llm_text, False
        if not isinstance(args, dict):
            args = {}
        result = call_tool(func, args)
        return result, True
    except json.JSONDecodeError:
        return llm_text, False
    except Exception as e:
        return f"error: {e}", True
