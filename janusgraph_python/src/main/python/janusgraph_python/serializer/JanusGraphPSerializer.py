from gremlin_python.structure.io.graphsonV3d0 import GraphSONUtil


class JanusGraphPSerializer(object):
    """
    This is serializer method being used to serialize P predicates as JanusGraphPSerializer, which is used by JanusGraph for all predicates,
    including Text
    """

    GRAPHSON_PREFIX = "janusgraph"
    GRAPHSON_BASE_TYPE = "JanusGraphP"

    @classmethod
    def dictify(cls, p, writer):
        """ Serializes JanusGrahP object.

        Args:
            p (JanusGraphPSerializer): The Predicate to serialize.
            writer:

        Returns:
            json
        """
        predicateJSON = cls.__predicate_to_dict(p)

        serializedJSON = GraphSONUtil.typed_value(cls.GRAPHSON_BASE_TYPE, predicateJSON, cls.GRAPHSON_PREFIX)
        return serializedJSON

    @classmethod
    def __predicate_to_dict(cls, p):

        predicateDict = dict()

        predicateDict["predicate"] = p.operator
        predicateDict["value"] = p.value

        return predicateDict

