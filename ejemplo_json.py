import json
acciones={"AENA.MC":143.75,"BBVA.MC":6.34,"REP.MC":14.22,"SAN.MC":3.324}
s=json.dumps(acciones)
print(type(s))
print(s)

dicc=json.loads(s)
print(type(dicc))
print(dicc)
