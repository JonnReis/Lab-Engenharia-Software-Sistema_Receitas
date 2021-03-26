from flask import Blueprint, render_template, request

ingredient_controller = Blueprint('ingredient', __name__, url_prefix='/ingredients')


@ingredient_controller.route('/')
def index():
    ingredients = get_ingredients()
    return render_template('ingredient/ingredient.html', title='Ingredientes', data={'ingredients': ingredients})


@ingredient_controller.route('/create', methods=['GET', 'POST'])
def create_ingredients():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
    return render_template('ingredient/create-ingredient/create-ingredient.html', title='Adicionar ingredientes')


@ingredient_controller.route('/edit', methods=['GET', 'PUT'])
def update_ingredients():
    stored_ingredients = get_ingredients()
    if request.method == 'PUT':
        ingredients = request.form.get('ingredients')
    return render_template('ingredient/edit-ingredient/edit-ingredient.html', title='Editar ingredientes',
                           data={'ingredients': stored_ingredients})


@ingredient_controller.route('/getIngredients')
def get_ingredients():
    return [
        {
            'id': 1,
            'name': 'Ovo',
        },
        {
            'id': 2,
            'name': 'Achocolatado',
        },
        {
            'id': 3,
            'name': 'Manteiga',
        },
        {
            'id': 4,
            'name': 'Óleo',
        },
        {
            'id': 5,
            'name': 'Farinha de trigo',
        },
        {
            'id': 6,
            'name': 'Açucar',
        },
        {
            'id': 7,
            'name': 'Fermento',
        },
        {
            'id': 8,
            'name': 'Leite',
        },
        {
            'id': 9,
            'name': 'Leite condensado',
        },
        {
            'id': 10,
            'name': 'Biscoito de maizena',
        },
        {
            'id': 11,
            'name': 'Margarina',
        },
        {
            'id': 12,
            'name': 'Creme de leite',
        },
        {
            'id': 13,
            'name': 'Suco de limão',
        },
        {
            'id': 14,
            'name': 'Raspa de limão',
        },
        {
            'id': 15,
            'name': 'Clara de ovo',
        }
    ]
