import json

def handler(request):
    # Parse query parameters
    query = request.query_params
    names = query.getlist("name")

    # Load data
    with open("q-vercel-python.json", "r") as f:
        students = json.load(f)

    # Create a dict for faster lookup
    marks_dict = {student["name"]: student["marks"] for student in students}

    # Get marks in requested order
    result = [marks_dict.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": json.dumps({ "marks": result })
    }
