import ast
import operator as op

_ALLOWED = {
    ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
    ast.Pow: op.pow, ast.USub: op.neg, ast.Mod: op.mod, ast.FloorDiv: op.floordiv
}

def _eval(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.Expr):
        return _eval(node.value)
    raise ValueError("unsupported expression")

def calculate(expression):
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval(tree.body)
        return str(result)
    except Exception as e:
        return f"couldnt evaluate expression! ({e})"

def search_arxiv(query):
    return f"arxive related to:'{query}']"

TOOLS = {
    "calculate": calculate,
    "search_arxiv": search_arxiv
}

def call_tool(func_name, args):
    fn = TOOLS.get(func_name)
    if not fn:
        return f"Error '{func_name}'"
    try:
        return fn(**args)
    except TypeError as te:
        return f"error; '{func_name}' ({te})"
    except Exception as e:
        return f"error: {e}"
