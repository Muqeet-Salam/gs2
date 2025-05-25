import json
import os

def handler(request):
    query = request.query_params
    names = query.getlist("name")

    try:
        json_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
        with open(json_path, "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        return {
            "statusCode": 500,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps({ "error": "Data file not found." })
        }

    marks_dict = {student["name"]: student["marks"] for student in students}
    result = [marks_dict.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({ "marks": result })
    }
