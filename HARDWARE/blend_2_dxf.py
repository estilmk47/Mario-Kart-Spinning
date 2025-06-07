import bpy
import bmesh
import os
import sys

# Add venv site-packages to sys.path
project_dir = os.path.dirname(bpy.data.filepath)
venv_site_packages = os.path.join(project_dir, '.venv', 'Lib', 'site-packages')
if venv_site_packages not in sys.path:
    sys.path.append(venv_site_packages)

import ezdxf
# from mathutils import Vector

def export_object_to_dxf(obj_name: str, output_path: str, scale=1.0):
    obj = bpy.data.objects.get(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found.")
    
    if obj.type != 'MESH':
        raise TypeError(f"Object '{obj_name}' is not a mesh.")

    bpy.ops.object.mode_set(mode='OBJECT')

    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.edges.ensure_lookup_table()

    # Create a new DXF document
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Convert edges to DXF lines
    for edge in bm.edges:
        verts = edge.verts
        start = verts[0].co  # Start vertex of the edge
        end = verts[1].co    # End vertex of the edge
        msp.add_line(start=(start.x*scale, start.y*scale), end=(end.x*scale, end.y*scale))

    # Save the DXF file
    doc.saveas(output_path)
    print(f"Edges of object '{obj.name}' successfully exported to '{output_path}'.")
    bm.free()

    # mesh = obj.data
    # mesh.calc_loop_triangles()

    # world_matrix = obj.matrix_world

    # doc = ezdxf.new(dxfversion='R2010')
    # msp = doc.modelspace()

    # visited_edges = set()
    # for edge in mesh.edges:
    #     v1 = world_matrix @ mesh.vertices[edge.vertices[0]].co
    #     v2 = world_matrix @ mesh.vertices[edge.vertices[1]].co
    #     edge_key = tuple(sorted((edge.vertices[0], edge.vertices[1])))
    #     if edge_key not in visited_edges:
    #         msp.add_3dpolyline([v1[:], v2[:]])
    #         visited_edges.add(edge_key)

    # doc.saveas(output_path)
    # print(f"Exported '{obj_name}' to DXF at '{output_path}'")

if __name__ == '__main__':
    obj_name = "JC"
    export_object_to_dxf(obj_name, os.path.join(project_dir, 'output', f"{obj_name}.dxf"))