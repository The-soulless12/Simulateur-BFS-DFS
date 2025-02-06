from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def bfs(graph, start):
    visited = []
    queue = [start]
    history = {"queue": [], "visited": []}

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)
        history["queue"].append(queue[:])  
        history["visited"].append(visited[:])
    
    return history

def dfs(graph, start):
    visited = set()
    stack = [start]
    history = {"stack": [], "visited": []}

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)
        history["stack"].append(stack[:])
        history["visited"].append(list(visited))
    
    return history

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    algorithm = data.get("algorithm")
    graph = data.get("graph")
    start = data.get("start")

    if not graph or not start:
        return jsonify({"error": "Graph or start node missing"}), 400

    if algorithm == "BFS":
        result = bfs(graph, start)
    elif algorithm == "DFS":
        result = dfs(graph, start)
    else:
        return jsonify({"error": "Invalid algorithm"}), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)