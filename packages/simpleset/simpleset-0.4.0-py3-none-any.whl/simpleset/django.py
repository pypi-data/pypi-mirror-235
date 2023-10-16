from django.db.models import CharField

from simpleset import Constant


class ConstantField( CharField ):
    def __init__( self, *args, **kwargs ):
        if args and issubclass( args[0], Constant ):
            self.object_class = args[0]
            kwargs[ "choices"    ] = self.object_class.choices
            kwargs[ "max_length" ] = self.object_class.max_length()
            kwargs[ "validators" ] = [ self.object_class.validate ]
            if "default" in kwargs:
                kwargs[ "default" ] = str( kwargs[ "default" ] )
            if "null" in kwargs:
                kwargs[ "blank" ] = kwargs[ "null" ]
        super().__init__( *args[ 1: ], **kwargs )

    def deconstruct( self ):
        name, path, args, kwargs = super().deconstruct()
        for attr in ( "blank", "choices", "validators" ):
            if attr in kwargs:
                del kwargs[ attr ]
        args = [ self.object_class ]
        return name, path, args, kwargs

    # DB -> Python
    def from_db_value( self, value, expression, connection ):
        if value is None:
            return value
        return self.object_class.wrap( value )

    # DB -> Python
    def to_python( self, value ):
        if value is None:
            return value
        return self.object_class.wrap( value )

    # Python -> DB
    def get_prep_value( self, value ):
        if value is None:
            return value
        self.object_class.wrap(value)  # validate before save
        return str(value)
