from flask import Blueprint, render_template, request

from src.controller.ingredientController import get_ingredients

recipe_controller = Blueprint('recipe', __name__, url_prefix='/recipes')


@recipe_controller.route('/')
def index():
    recipes = get_recipes()
    return render_template('recipe/recipe.html', title='Receitas', data={'recipes': recipes})


@recipe_controller.route('/create', methods=['GET', 'POST'])
def create_recipe():
    if request.method == 'POST':
        name = request.form.get('name')
        ingredients = request.form.get('ingredients')

    stored_ingredients = get_ingredients()
    return render_template('recipe/create-recipe/create-recipe.html', data={'stored_ingredients': stored_ingredients})


@recipe_controller.route('/edit/<id>')
def get_recipe_by_id(id):
    recipes = get_recipes()
    recipe = find_recipe(recipes, id)
    return render_template('recipe/edit-recipe/edit-recipe.html', data={'recipe': recipe})


@recipe_controller.route('/getRecipes', methods=['GET'])
def get_recipes():
    return [
        {
            'id': 1,
            'name': 'Torta de limão',
            'ingredients': {
                'Biscoito de maizena': '200g',
                'Margarina': '150g',
                'Leite condensado': '1 lata(395g)',
                'Creme de leite':'1 caixa(200g)',
                'Suco de limão':'4 limões',
                'Raspas de limão':'2 limões',
                'Claras de ovo':'3 ou 4',
                'Açúcar':'3 colheres (sopa)'
            },
            'steps': '1 - Triturar biscoito, 2 - Juntar tudo e bater, 3 - Despejar na forma, 4 - Levar ao forno médio (180º C)',
            'created-at': '22/03/2021'
        },
        {
            'id': 2,
            'name': 'Bolo de chocolate',
            'ingredients': {
                'Ovo': '4',
                'Achocolatado em pó': '2 colheres (sopa)',
                'Manteiga':'2 colheres (sopa)',
                'Oléo': '1 xícara',
                'Farinha de trigo':'3 xícaras (chá)',
                'Açucar':'2 xícaras (chá)',
                'Fermento':'2 colheres (sopa)',
                'Leite':'1 xícara (chá)',
                'Leite condensado': '1'
            },
            'steps': '1 - Bater no liquidificador, 2 - Despejar na forma, 3 - Assar em fogo médio',
            'created-at': '22/03/2021'
        },
        {
            'id':3,
            'name':'teste1',
            'ingredients':{
                'teste1':'1',
                'teste2':'2',
                'teste3':'3'
            },
            'steps':'teste1, teste2, teste3',
            'created-at':'25/03/2021'
        },
        {
            'id':4,
            'name':'teste2',
            'ingredients':{
                'teste1':'1',
                'teste2':'2',
                'teste3':'3'
            },
            'steps':'teste1, teste2, teste3',
            'created-at':'25/03/2021'
        }
    ]


def find_recipe(recipe_list, recipe_id):
    recipe_id = int(recipe_id)
    for recipe in recipe_list:
        if recipe['id'] == recipe_id:
            return recipe
   