from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int , b:int)->int:
    """ 
    Add two numbers together
    """
    return a+b

@mcp.tool()
def subtract(a:int,b:int)->int:
    """
    Subtract two numbers
    
    """
    return a-b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """ Multiply two numbers """
    return a*b

if __name__=="__main__":
# the transport = stdio tells the server to use standard input/output to receive and respond to tool functional calls
    mcp.run(transport="stdio")