def parse(cls, s):
    length = read_varints(s)
    cmds = []
    count = 0
    while count < length:
        current = s.read(1)
        count += 1
        current_byte = current[0]
        if current_byte >= 1 and current_byte <= 75:
            n = current_byte
            cmds.append(s.read(n))
            count += n
        elif current_byte == 76:
            data_length = little_endian_to_int(s.read(1))
            cmds.append(s.read(data_length))
            count += n
        else:
            op_code = current_byte
            cmds.append(op_code)
        if count != length:
            raise SyntaxError('parsing script failed')
        return cls(cmds)
        
