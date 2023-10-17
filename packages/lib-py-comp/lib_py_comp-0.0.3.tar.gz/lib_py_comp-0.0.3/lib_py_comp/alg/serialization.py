import lib_py_comp.alg.typon_math as typon_math
import lib_py_parse.utils.parsing_utils as parsing_utils

def serialize_data(target_value, target_type, classes, str_encoding='latin-1'):
    target_type = target_type.replace(' ', '')

    if target_type == 'bool':
        result = b'\x00'
        if target_value:
            result = b'\x01'
        return result

    if target_type == 'char':
        X1 =  str(target_value)
        if len(X1) != 1:
            return b'\x00'

        try:
            return X1.encode('latin-1')
        except Exception as e:
            return X1.encode()

    if target_type == 'int':
        result = typon_math.serialize_int(target_value)
        return result

    if target_type == 'dbl':
        result = typon_math.serialize_dbl(target_value)
        return result

    if target_type == 'str':
        result = None
        if isinstance(target_value, bytes):
            result = typon_math.serialize_int( len(target_value) ) + target_value
        else:
            try:
                x1 = target_value.encode(str_encoding)
                result = typon_math.serialize_int( len(x1) ) + x1
            except Exception as e:
                x1 = target_value.encode()
                result = typon_math.serialize_int( len(x1) ) + x1
        return result

    if target_type[0:4] == 'vec[':
        result = typon_math.serialize_int( len(target_value) )
        item_type = target_type[4:-1]
        for i in range(0, len(target_value)):
            result += serialize_data( target_value[i], item_type, classes, str_encoding=str_encoding )
        return result

    if target_type[0:5] in ['hmap[', 'smap[']:
        delimited_types = target_type[5:-1]
        key_type, value_type = parsing_utils.read_delimited_types(delimited_types)
        result = typon_math.serialize_int( len(target_value) )
        for key_var in target_value:
            result += serialize_data( key_var, key_type, classes, str_encoding=str_encoding )
            result += serialize_data( target_value[key_var], value_type, classes, str_encoding=str_encoding )
        return result

    if target_type[0:5] == 'tupl[':
        delimited_types = target_type[5:-1]
        typon_tuple_types = parsing_utils.read_delimited_types(delimited_types)
        result = b''
        for i in range(0, len(typon_tuple_types)):
            result += serialize_data( target_value[i], typon_tuple_types[i], classes, str_encoding=str_encoding )
        return result

    if target_type in classes:
        class_items = classes[target_type]
        result = b''
        for attr_name in class_items:
            attr_value = eval( f'target_value.{attr_name}' )
            attr_type = class_items[attr_name]
            result += serialize_data( attr_value, attr_type, classes, str_encoding=str_encoding )
        return result

    raise Exception(f'unverified type in fxn serialize_data: {target_type}')
