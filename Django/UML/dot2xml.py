import os
import django
import pydot
from django.apps import apps

# Initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace 'your_project.settings' with your settings module
django.setup()

def get_class_details(model):
    fields = [f.name for f in model._meta.get_fields()]
    methods = [method for method in dir(model) if callable(getattr(model, method)) and not method.startswith("__")]
    return fields, methods

def dot_to_drawio(dot_file_path, drawio_file_path, models):
    graphs = pydot.graph_from_dot_file(dot_file_path)
    graph = graphs[0]

    drawio_xml = '<mxfile host="app.diagrams.net">\n'
    drawio_xml += '<diagram name="Page-1">\n'
    drawio_xml += '<mxGraphModel dx="1034" dy="532" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">\n'
    drawio_xml += '<root>\n'
    drawio_xml += '<mxCell id="0"/>\n'
    drawio_xml += '<mxCell id="1" parent="0"/>\n'

    node_id_map = {}
    node_id = 2
    for node in graph.get_nodes():
        node_name = node.get_name().strip('"')
        node_id_map[node_name] = str(node_id)

        if node_name in models:
            fields, methods = get_class_details(models[node_name])
            tooltip = f'Fields: {", ".join(fields)}\nMethods: {", ".join(methods)}'
        else:
            tooltip = 'No details available'

        drawio_xml += f'<mxCell id="{node_id}" value="{node_name}" style="shape=rectangle;" vertex="1" parent="1" tooltip="{tooltip}">\n'
        drawio_xml += '<mxGeometry x="10" y="10" width="150" height="100" as="geometry"/>\n'
        drawio_xml += '</mxCell>\n'
        node_id += 1

    edge_id = node_id
    for edge in graph.get_edges():
        src = edge.get_source().strip('"')
        dst = edge.get_destination().strip('"')
        src_id = node_id_map.get(src)
        dst_id = node_id_map.get(dst)
        if src_id and dst_id:
            drawio_xml += f'<mxCell id="{edge_id}" source="{src_id}" target="{dst_id}" edge="1" parent="1">\n'
            drawio_xml += '<mxGeometry relative="1" as="geometry"/>\n'
            drawio_xml += '</mxCell>\n'
            edge_id += 1

    drawio_xml += '</root>\n'
    drawio_xml += '</mxGraphModel>\n'
    drawio_xml += '</diagram>\n'
    drawio_xml += '</mxfile>\n'

    with open(drawio_file_path, 'w') as f:
        f.write(drawio_xml)

# Collect all models from all installed apps
models = {model.__name__: model for model in apps.get_models()}

dot_to_drawio('my_project.dot', 'my_project.drawio', models)
