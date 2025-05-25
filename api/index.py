import json

def handler(request):
    print("Received request:", request)

    # Load JSON data from local file
    with open("q-vercel-python.json", "r") as f:
        data_list = json.load(f)

    # Convert to a dictionary: { name: marks }
    data = {entry["name"]: entry["marks"] for entry in data_list}
    print("Data dictionary:", data)

    # Extract query parameters
    query_params = request.get("queryStringParameters", {})
    names = query_params.get("name")

    # Handle multiple ?name=...&name=... values (vercel sends as list if multiple)
    if names is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No name parameters provided"}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    if isinstance(names, str):
        names = [names]  # single value case
    print("Processed names:", names)

    # Get marks for each name (default to 0 if not found)
    marks = [data.get(name, 0) for name in names]
    print("Marks:", marks)

    return {
        "statusCode": 200,
        "body": json.dumps({"marks": marks}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET"
        }
    }

handler.__name__ = "handler"
