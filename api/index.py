import json

def handler(request):
    # Load data
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)
    
    # Get list of names from query params
    names = request.get("queryStringParameters", {}).get("name")

    if not names:
        return {
            "statusCode": 400,
            "body": json.dumps({ "error": "No name parameters provided" }),
            "headers": { "Content-Type": "application/json" }
        }

    # If only one name, convert to list
    if isinstance(names, str):
        names = [names]

    # Get marks in order
    marks = [data.get(name, 0) for name in names]

    return {
        "statusCode": 200,
        "body": json.dumps({ "marks": marks }),
        "headers": { "Content-Type": "application/json" }
    }

# Vercel requires this name
handler.__name__ = "handler"
