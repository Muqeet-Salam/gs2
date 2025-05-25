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

    # Get 'name' parameter from query string
    names_param = request.get("queryStringParameters", {}).get("name")
    print("Query parameter 'name':", names_param)

    if not names_param:
        print("No name parameters provided in the request.")
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No name parameters provided"}),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    # If multiple names passed as comma-separated string, split them
    if isinstance(names_param, str):
        names = [name.strip() for name in names_param.split(",")]
    else:
        names = []

    print("Processed names list:", names)

    # Lookup marks for each name; default 0 if not found
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
