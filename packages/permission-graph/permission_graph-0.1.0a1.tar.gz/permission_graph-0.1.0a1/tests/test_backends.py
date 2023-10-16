import pytest

from permission_graph import EdgeType, Group, Resource, ResourceType, Actor
from permission_graph.backends import (IGraphMemoryBackend,
                                       PermissionGraphBackend)


@pytest.mark.integration
@pytest.mark.parametrize("backend", [IGraphMemoryBackend()])
def test_backend(backend: PermissionGraphBackend):
    """A simple test that any valid backend should pass."""

    # Add a vertex to the graph
    actor = Actor("Alice")
    backend.add_vertex(actor)
    assert backend.vertex_exists(actor)

    # Vertexes are unique
    with pytest.raises(ValueError):
        backend.add_vertex(actor)

    # Add a second vertex and an edge between it and the first
    group = Group("Admins")
    backend.add_vertex(group)
    with pytest.raises(ValueError):
        backend.get_edge_type(actor, group)

    backend.add_edge(EdgeType.MEMBER_OF, actor, group)
    assert backend.edge_exists(actor, group)
    assert backend.get_vertices_to(group) == [actor]
    assert backend.get_edge_type(actor, group) == EdgeType.MEMBER_OF

    # Edges are unique
    with pytest.raises(ValueError):
        backend.add_edge(EdgeType.MEMBER_OF, actor, group)

    # Add third vertex and two edges
    resource = Resource("foo", ResourceType("Foo", ["bar"]))
    backend.add_vertex(resource)
    backend.add_edge(EdgeType.DENY, group, resource)
    backend.add_edge(EdgeType.ALLOW, actor, resource)

    assert backend.shortest_path(actor, resource) == [actor, resource]

    # Remove an edge
    backend.remove_edge(actor, group)
    assert not backend.edge_exists(actor, group)

    # Remove a vertex
    backend.remove_vertex(actor)
    assert not backend.vertex_exists(actor)
