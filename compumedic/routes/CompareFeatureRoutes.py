from flask import Blueprint, request, render_template

# Logger
from compumedic.utils.Logger import Logger
from compumedic.models.CompareFeatureModels import get_store_by_id
from compumedic.services.scrapping.BoticasPeruScrapperQueryImp import BoticasPeruScrapperQueryImp
from compumedic.services.scrapping.FarmaciaUniversalQueryImp import FarmaciaUniversalQueryImp
from compumedic.services.scrapping.BoticasHogarYSaludQueryImp import BoticasHogarYSalud
from compumedic.services.scrapping.InkaFarmaQueryImp import InkaFarmaQueryImp
from compumedic.services.scrapping.BoticasYSaludQueryImp import BoticasYSaludQueryImp
from compumedic.services.scrapping.MiFarmaQueryImp import MiFarmaQueryImp

compare = Blueprint('compare_feature_blueprint', __name__, static_folder='../static')


@compare.get('/')
def index():
    # try:
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    query = request.args.get('query', '')
    inst_bp = BoticasPeruScrapperQueryImp(query=query)
    inst_bp.execute_query()

    inst_fu = FarmaciaUniversalQueryImp(query=query)
    inst_fu.execute_query()

    inst_bhs = BoticasHogarYSalud(query=query)
    inst_bhs.execute_query()

    inst_mf = MiFarmaQueryImp(query=query)
    inst_mf.execute_query()

    inst_ik = InkaFarmaQueryImp(query=query)
    inst_ik.execute_query()

    inst_bs = BoticasYSaludQueryImp(query=query)
    inst_bs.execute_query()

    list_stores = [
        {
            'name': get_store_by_id(1).name,
            'photo': get_store_by_id(1).logo,
            'product': inst_mf.get_result()
        },
        {
            'name': get_store_by_id(2).name,
            'photo': get_store_by_id(2).logo,
            'product': inst_bhs.get_result()
        },
        {
            'name': get_store_by_id(3).name,
            'photo': get_store_by_id(3).logo,
            'product': inst_ik.get_result()
        },
        {
            'name': get_store_by_id(4).name,
            'photo': get_store_by_id(4).logo,
            'product': inst_bs.get_result()
        },
        {
            'name': get_store_by_id(5).name,
            'photo': get_store_by_id(5).logo,
            'product': inst_fu.get_result()
        },
        {
            'name': get_store_by_id(6).name,
            'photo': get_store_by_id(6).logo,
            'product': inst_bp.get_result()
        }
    ]
    return render_template('compare_product.jinja2',
                           titulo="OCR Flask",
                           q=query,
                           stores=list_stores)
# except Exception as ex:
#    Logger.add_to_log("error", str(ex))
#    Logger.add_to_log("error", traceback.format_exc())
#    response = jsonify({'message': "Internal Server Error", 'success': False})
#    raise ex
#    return response
