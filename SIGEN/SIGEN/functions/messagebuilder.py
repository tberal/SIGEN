from SIGEN.configs import entrada, saida, receituario

def Build(ftype, mvtList):
    if ftype == 'E':
        msgs = [{x: (item[y] if isinstance(y, int) else y) for x, y in entrada.items()} for item in mvtList]
    else:
        if ftype == 'S':
            msgs = [{x: (item[y] if isinstance(y, int) else y) for x, y in saida.items()} for item in mvtList]
        else:
            msgs = []
            for item in mvtList:
                if item[0] == 'R':
                    msgs.append({x: (item[y] if isinstance(y, int) else y) for x, y in receituario['header'].items()})
                else:
                    msgs[-1]['listaDiagnosticos'].append({x: (item[y] if isinstance(y, int) else y) for x, y in receituario['item'].items()})
    return msgs
