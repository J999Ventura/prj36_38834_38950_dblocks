from v1.routes import v1_bp

@v1_bp.route("/", methods=['GET'])
def get_api_routes():
    return "Documentacao API (rotas)"