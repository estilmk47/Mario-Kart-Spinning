import numpy as np

def calculate_normal_vector(p1, p2, p3):
    """
    Calculate the normal vector to the plane defined by three 3D points.
    
    Args:
        p1, p2, p3: Tuples or lists of (x, y, z) coordinates.
    
    Returns:
        A NumPy array representing the normal vector.
    """
    # Create vectors from the points
    v1 = np.array(p2) - np.array(p1)
    v2 = np.array(p3) - np.array(p1)
    
    # Compute the cross product
    normal = np.cross(v1, v2)
    
    return normal

def angle_between_vectors(v1, v2):
    """
    Calculate the angle (in degrees) between two vectors.
    
    Args:
        v1, v2: Tuples, lists, or arrays representing vectors.
    
    Returns:
        Angle in degrees.
    """
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    # Normalize the vectors
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    
    if v1_norm == 0 or v2_norm == 0:
        raise ValueError("One of the vectors is zero-length")
    
    # Compute dot product and angle
    dot_product = np.dot(v1, v2)
    cosine_angle = np.clip(dot_product / (v1_norm * v2_norm), -1.0, 1.0)
    angle_rad = np.arccos(cosine_angle)
    
    # Convert to degrees
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

# Example usage
if __name__ == "__main__":
    p1 = (11, 0.467717, -0.608033)
    p2 = (11, -2.86562, 3.7253)
    p3 = (-11, -2.86562, 3.7253)
    n = calculate_normal_vector(p2, p1, p3)
    print("Normal Vector:", n)

    v1 = [n[0], n[1], n[2]]
    v2 = [0, 0, 1]
    angle = angle_between_vectors(v1, v2)
    print("Angle between vectors (degrees):", angle)
