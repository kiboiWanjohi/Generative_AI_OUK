"""Build Code Context Graph and generate diagrams"""

def build_ccg(code_structure):
    """Build relationships between code elements"""
    ccg = {
        "nodes": [],
        "edges": [],
        "relationships": []
    }
    
    for cls in code_structure.get("classes", []):
        ccg["nodes"].append({
            "id": f"class_{cls['name']}",
            "label": cls['name'],
            "type": "class",
            "module": cls['module']
        })
    
    for func in code_structure.get("functions", []):
        ccg["nodes"].append({
            "id": f"func_{func['name']}",
            "label": func['name'],
            "type": "function",
            "module": func['module']
        })
    
    for i, func in enumerate(code_structure.get("functions", [])):
        if i > 0:
            ccg["edges"].append({
                "source": f"func_{code_structure['functions'][i-1]['name']}",
                "target": f"func_{func['name']}",
                "relation": "calls"
            })
    
    return ccg

def generate_mermaid_diagram(ccg):
    """Generate Mermaid diagram from CCG"""
    lines = ["```
    
    for node in ccg["nodes"][:10]:
        node_id = node["id"].replace("_", "")
        label = node["label"]
        if node["type"] == "class":
            lines.append(f'    {node_id}["<b>{label}</b><br/>(class)"]:::class')
        else:
            lines.append(f'    {node_id}["{label}()"]:::function')
    
    for edge in ccg["edges"][:8]:
        src = edge["source"].replace("_", "")
        tgt = edge["target"].replace("_", "")
        lines.append(f'    {src} -->|{edge["relation"]}| {tgt}')
    
    lines.append('    classDef class fill:#e1f5ff,stroke:#01579b,stroke-width:2px')
    lines.append('    classDef function fill:#f3e5f5,stroke:#4a148c,stroke-width:2px')
    lines.append("```")
    
    return "\n".join(lines)
