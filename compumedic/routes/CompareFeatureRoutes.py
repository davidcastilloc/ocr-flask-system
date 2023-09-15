from flask import Blueprint, request, render_template

# Logger
from compumedic.utils.Logger import Logger
from compumedic.models.CompareFeatureModels import get_store_by_id
from compumedic.services.scrapping.BoticasPeruScrapperQueryImp import BoticasPeruScrapperQueryImp
from compumedic.services.scrapping.FarmaciaUniversalQueryImp import FarmaciaUniversalQueryImp

compare = Blueprint('compare_feature_blueprint', __name__, static_folder='../static')


@compare.get('/')
def index():
    # try:
    Logger.add_to_log("info", "{} {}".format(request.method, request.path))
    query = request.args.get('query', '')
    inst_bp = BoticasPeruScrapperQueryImp()
    inst_bp.execute_query()

    inst_fu = FarmaciaUniversalQueryImp()
    inst_fu.execute_query()


    list_stores = [
        {
            'name': get_store_by_id(1).name,
            'photo': get_store_by_id(1).logo,
            'product': inst_bp.get_result()
        },
        {
            'name': get_store_by_id(2).name,
            'photo': get_store_by_id(2).logo,
            'product': inst_bp.get_result()
        },
        {
            'name': get_store_by_id(3).name,
            'photo': get_store_by_id(3).logo,
            'product': inst_bp.get_result()
        },
        {
            'name': get_store_by_id(4).name,
            'photo': get_store_by_id(4).logo,
            'product': inst_bp.get_result()
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
