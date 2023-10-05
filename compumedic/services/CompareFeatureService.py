from compumedic.services.scrapping.BoticasHogarYSaludQueryImp import BoticasHogarYSalud
from compumedic.services.scrapping.BoticasPeruScrapperQueryImp import BoticasPeruScrapperQueryImp
from compumedic.services.scrapping.BoticasYSaludQueryImp import BoticasYSaludQueryImp
from compumedic.services.scrapping.FarmaciaUniversalQueryImp import FarmaciaUniversalQueryImp
from compumedic.services.scrapping.InkaFarmaQueryImp import InkaFarmaQueryImp
from compumedic.services.scrapping.MiFarmaQueryImp import MiFarmaQueryImp

def get_data(query):
    inst_bp = BoticasPeruScrapperQueryImp(query=query)
    inst_fu = FarmaciaUniversalQueryImp(query=query)
    inst_bhs = BoticasHogarYSalud(query=query)
    inst_mf = MiFarmaQueryImp(query=query)
    inst_ik = InkaFarmaQueryImp(query=query)
    inst_bs = BoticasYSaludQueryImp(query=query)

    data = []

    # Define una función para ejecutar la consulta y agregar el resultado al diccionario
    def execute_and_append_result(inst, name, photo, data):
        try:
            inst.execute_query()
            data.append({
                'name': name,
                'photo': photo,
                'product': inst.get_result()
            })
        except Exception as e:
            # Puedes manejar la excepción aquí si lo necesitas
            print(f"Error al ejecutar {name}: {str(e)}")

    # Ejecuta y agrega los resultados al diccionario
    execute_and_append_result(inst_mf, "MiFarma", "Mifarma.png", data)
    execute_and_append_result(inst_bhs, "BoticasHogarYSalud", "BoticasHogarYSalud.png", data)
    execute_and_append_result(inst_ik, "InkaFarma", "Inkafarma.png", data)
    execute_and_append_result(inst_bs, "BoticasYSalud", "BoticasYSalud.png", data)
    execute_and_append_result(inst_fu, "FarmaciaUniversal", "FarmaciaUniversal.png", data)
    execute_and_append_result(inst_bp, "BoticasPeru", "BoticasPeru.png", data)

    return data
