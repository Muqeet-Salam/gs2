import json
import os

def handler(request):
    print("Received request:", request)

    # Load data file path (adjust if needed)
    json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

    # Load data as list of dicts
    with open(json_path, "r") as f:
        data_list = json.load(f)
    print("Loaded data list:", data_list)

    # Convert list of dicts to dict for fast lookup
    data = {entry["name"]: entry["marks"] for entry in data_list}
    print("Converted data dict:", data)

    # Get list of names from query params
    names = request.get("queryStringParameters", {}).get("name")
    print("Query parameter 'name':", names)

    if not names:
        print("No name parameters provided in the request.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No name parameters provided"}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    # If only one name, convert to list
    if isinstance(names, str):
        names = [names]
    print("Processed names list:", names)

    # Get marks in order
    marks = []
    for name in names:
        mark = data.get(name, 0)
        print(f"Mark for {name}: {mark}")
        marks.append(mark)

    print("Final marks list:", marks)

    return {
        "statusCode": 200,
        "body": json.dumps({"marks": marks}),
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }
    }

handler.__name__ = "handler"

